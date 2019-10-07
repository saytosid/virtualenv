"""Bootstrap"""
from __future__ import absolute_import, unicode_literals

import logging
import os
import shutil
import sys
import zipfile
from shutil import copytree
from textwrap import dedent

from pathlib2 import Path
from six import PY3

from virtualenv.info import get_default_data_dir

from .wheels.acquire import get_wheel

try:
    import ConfigParser
except ImportError:
    # noinspection PyPep8Naming
    import configparser as ConfigParser


def bootstrap(creator):
    cache = get_default_data_dir() / "seed-v1"
    name_to_whl = get_wheel(creator, cache)
    install_image = (
        cache / "install" / creator.interpreter.implementation.lower() / creator.interpreter.version_release_str
    )
    install_image.mkdir(parents=True, exist_ok=True)
    pip_install(name_to_whl, creator, install_image)


def pip_install(wheels, creator, install_image):
    site_package, bin_dir, env_exe = creator.site_packages[0], creator.bin_dir, creator.env_exe
    for name, wheel in wheels.items():
        logging.debug("install %s from wheel %s", name, wheel)
        target = install_image / wheel.name
        if not target.exists():
            dist_info, console_script = create_image(target, wheel, bin_dir, site_package)
        else:
            logging.debug("install from image %s", target)
            dist_info = get_dist_info(target)
            console_script = load_console_scripts(bin_dir, dist_info)
        for filename in target.iterdir():
            into = site_package / filename.name
            if into.exists():
                if into.is_dir() and not into.is_symlink():
                    shutil.rmtree(str(into))
                else:
                    into.unlink()
            method = link_method(filename)
            method(str(filename), str(into))
        for exe, (module, func) in console_script.items():
            write_entry_point(env_exe, exe, func, module)


def link_method(filename):
    if sys.platform != "win32":
        return os.symlink
    if filename.is_dir():
        if sys.version_info[0:2] > (3, 4):
            import _winapi

            return _winapi.CreateJunction
        else:
            return copytree
    else:
        return os.link


def create_image(target, wheel, bin_dir, site_package):
    logging.debug("create install image to %s of %s", target, wheel)
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(str(wheel)) as zip_ref:
        zip_ref.extractall(str(target))
    dist_info = get_dist_info(target)
    installer = dist_info / "INSTALLER"
    installer.write_text("pip\n")
    console_scripts = load_console_scripts(bin_dir, dist_info)
    fix_records(console_scripts, dist_info, target, os.path.relpath(str(bin_dir), str(site_package)))
    return dist_info, console_scripts


def add_record_line(name):
    return "{},,".format(name)


def fix_records(console_scripts, dist_info, target, bin_rel_to_site):
    # inject a no-op root element, as workaround for bug added by https://github.com/pypa/pip/commit/c7ae06c79#r35523722
    marker = target / "{}.virtualenv".format(target.name)
    marker.write_text("")

    # root elements
    new_records = [add_record_line(f.name) for f in target.iterdir()]
    # inject console scripts
    for exe in console_scripts:
        new_records.append("{},,".format(Path(bin_rel_to_site) / exe.name))
    record = dist_info / "RECORD"
    content = "\n".join(new_records)
    record.write_text(content)


def get_dist_info(target):
    return next(i for i in target.iterdir() if i.suffix == ".dist-info")


def load_console_scripts(bin_dir, dist_info):
    result = {}
    entry_points = dist_info / "entry_points.txt"
    if entry_points.exists():
        parser = ConfigParser.ConfigParser()
        with entry_points.open() as file_handler:
            reader = getattr(parser, "read_file" if PY3 else "readfp")
            reader(file_handler)
        if "console_scripts" in parser.sections():
            for exe_name, value in parser.items("console_scripts"):
                exe = bin_dir / "{}{}".format(exe_name, ".exe" if sys.platform == "win32" else "")
                module, func = value.split(":")
                result[exe] = module, func
    return result


def write_entry_point(env_exe, exe, func, module):
    content = (
        dedent(
            """
    #!{0}
    # -*- coding: utf-8 -*-
    import re
    import sys

    from {1} import {2}

    if __name__ == "__main__":
        sys.argv[0] = re.sub(r"(-script.pyw?|.exe)?$", "", sys.argv[0])
        sys.exit({2}())
    """
        )
        .lstrip()
        .format(env_exe, module, func)
    )
    exe.write_text(content)
    exe.chmod(0o755)
