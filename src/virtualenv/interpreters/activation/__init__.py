import sys
import os

from virtualenv.info import IS_WIN

def _convert(s):
    import base64
    import zlib
    b = base64.b64decode(s.encode("ascii"))
    return zlib.decompress(b).decode("utf-8")

# file activate.sh
ACTIVATE_SH = _convert(
    """
eJytVW1P2zAQ/u5fcaQVG9s6VvjGVLQyKoEELWo6JjZQMMmVWEudynYK5eW/75w3kgbYh9EPbe27
s5977p5zCyah0DAVEcIs0QauEBKNAdwIE4Kj40T5CFdCbnLfiAU36MCHqYpncMV1+IG1YBkn4HMp
YwMqkSAMBEKhb6IlY0xM4Tc47fu9vnvguaMf4++DzqMDPdr74sDFVzAhSgb0QT+MwTmjw1IY+cXG
gtO+EnOzA+ftYtsG765vZYG3dOX2NpsKxgIsUML7DbhP7YnUaKAzhfkyiH3Y3QxwsSmTKIKt3fUu
S31aoNB6xVEAKBdCxXKG0sCCK8GvItS51xpl07mD9v1pf/zRe4QLijOJkhqMShAoWzIAQQ7Qj7gi
GrkBHkVpOFnzeCLEGx3te6eH48mP/pF30p8c7NB5xAhUKLEfa+o57Ya7U3rg7TxWJnUs97KcG0Gp
nXj6B5qzycFoeDA6HrwAqbQ3gJWWJrzS9CrIupctaUZ82qQ6jBMqUICG2ivtP+AygDsdfoKbUPgh
hHyBwOmHTH48m1mzCakGtqfyo6jBfSoJ1cbEcE0IqH3o3zRWdjHn1Hx5qP4M8JNkECcmNxshr/Nj
ao6WIGhbisEPubxGDTekJx7YryVYbdC11GNzQo5BUQCiXxbq6KRUPzyUm79IMaeDsXs4GnaeK0Oa
ZEdRF5cdXSPtlQK73Rcq63YbJXW7zVq63VeLmJsLIJlLYR0MT5/SX7PYuvlEkLEMUJOQrIRxBV4L
XIymUDisrQDoWFOh/eL2R0bjKbMLpTDCBa9pujIt6nczVkHbczyvsvQ8h+U8VFNiDbERk5lQ80XF
e9Pz9g6H3rB/PPC8ndytquMS95MgLGG0w2plfU2qLwjLwlqR6epV6SjN2jO9pZr9/qHb3zsaeCfj
0fHJpNGYq43QsyBdW+Gnoju3T4RmxxCnsNaD2xc6suleOxQjjfWA95c0HFDyGcJ5jfhz53IDasH5
NKx0tk2+Bcf8D4JOFNrZkEgeCa7zF4SSEOadprmukAdLC1ghq3pUJFl9b9bXV04itdt3g7FsWT5Z
8yUNHQmdWe7ntL85WTe/yRx8gxn4n/Pvf2bfc3OPavYXWw6XFQ==
"""
)

# file activate.fish
ACTIVATE_FISH = _convert(
    """
eJytVm1v2zYQ/q5fcZUdyClqGVuHfQgwDGnjIQYSO3DcAMM6yLREWxxo0iMpty7243ekLImy5RQY
lg+xTd7rc3cPrweLnGlYM05hW2gDKwqFphn+Y2IDSy0LlVJYMTEiqWF7Ymi8ZjpfwtsvzORMAAFV
CGGF7TkMIDdmdzMa2V86p5zHqdzCNWiqNZPibRz04E6CkMYqAjOQMUVTww9xEKwLgV6kgGRFdM7W
h2RHTA7DDMKPUuypMhodOkfuwkjQckttIBuwKpASAWhObgT7RsMA8E9T41SOxvpEbfb1hVWqLhqh
P37400mspXKO8FAZwGx9mR/jeHiU67AW9psfN/3aSBkSFVn5meYSPMHAXngoWG+XUHDpnqPgwOlA
oXRlc4d/wCiIbiKIPovoxGVGqzpbf9H4KxZoz5QpCKdiD1uZUSAiQ+umUMK6NjnFaqot4ZgWikqx
pcLEkfPaQ0ELjOSZfwt7ohhZcaqdFFuDodh8Q4GwJbOHu+RlMl98un1Inm4X92ENcc81l8bu2mDz
FSvbWq7Rhq7T/K9M64Lq0U/vfwbCDVXY0tYW5Bg8R5xqm5XvQQnQb5Pn++RlPH+ezKYlUGEcQvhZ
hNfYFDDkBt7XulXZh5uvpfVBu2LnuVzXupRretnQuWajeOydWodCt7Ar7Hfg/X1xP5vezx7HYXAW
R313Gk198XocbbFXonGYP81nj0+LZIbYzyd3TTy22aru1DD8GxLsJQdzslNyuzNedzxjGNj5FE8P
wGWKLbl0E5tUFlxdlrZtCefyi2teRbdyj6JyDUvP7rLiQM87XcbtnDmcmw+8iMaKaOoNUKRPfJSz
pI1U1AUjFdswQXjjx3cPXXl7AukZOt/ToJfx9IvaVaJ2WY/SVfXH05d2uUPHPThDIbz5BSIhRYbH
qrBsQ6NWEfl6WN296Y55d8hk2n3VENiFdP2X5YKIP8R1li7THnwSNlOmFOV0T3wqiwOPPNv5BUE1
VR4+ECaJ9zNJQmv//2O4/8hsVaRnpILs1nqV+yWh1UR2WdFJOgBbJBf2vfRHSfJhMk2mt49jROKo
UuO97Dd0srQ9hYdxUH5aUjghm+5QPELrkqe+lfar2PTb7mByPBhuy7PjNuGka2L71s4suZs83354
GB/nJzw+jB/l7uBGPi2wmbCR2sRQ+yZIGaczeqSh1uT7Q3820y3xTk7AwSN72gqorw0xhX7n1iBP
R6MUsXub3nFywBXujBSt+1K5MuKT4lMZpMRNRjHcJ9DqHj+zXz2ZydquiO/gL7uU7hTdIcQuOH+L
EGRLG9/+w9JM1pG0kuaBc2VUTJg1RFf6Sked4jDAXJJUcsy9XG9eebsbc4MrfQ1RhzIMcHiojbjd
HaFntuLSEoJ5x7NQw1nr2NkOqV3T+g3qIQ54ubrXgp0032bvamC6yP4kaNfx/wIsXsYv
"""
)

# file activate.csh
ACTIVATE_CSH = _convert(
    """
eJx9VNtO4zAQffdXDKEiUEFhX8t22bJFWqRyEVuQVkKy3Hi6sZQ44Dit+sK379hJittG5KGqPZdz
fOZyCLNUlbBQGUJelRbmCFWJElbKphCVRWUShLnS5yKxaiksDpIyjaC/MEUO9Lc/YIfwt6ggEVoX
FkylQVmQymBis7Wz/jJIcRLma5iIpZIIEwXXmSgVfJf+Qs5//suFygZJkf8YMFaiBY2rTGkcxa8s
ZkxkSpQgsWUBsUVi27viD9MJf7l9mj2Pp/xxPPsNByO4gKMjoCSol+Dvot6e3/A9cl6VdmB71ksw
mIoyvYROnKeHu8dZiARvpMebHe0CeccvoLz9sjY5tq3h5v6lgY5eD4b9yGFFutCSrkzlRMAm554y
we3bWhYJqXcIzx5bGYMZLoW2sBRGiXmG5YAFsdsIvhA7rCDiPDhyHtXl2lOQpGhkZtuVCKKH7+ec
X9/e8/vx3Q3nw00EfWoBxwFWrRTBeSWiE7Apagb0OXRKz7XIEUbQFcMwK7HLOT6OtwlZQo9PIGao
pVrULKj64Ysnt3/G19ObtgkCJrXzF74jRz2MaCnJgtcN5B7wLfK2DedOp4vGydPcet5urq2XBEZv
DcnQpBZVJt0KUBqEa4YzpS0a3x7odFOm0Dlqe9oEkN8qVUlK01/iKfSa3LRRKmqkBc2vBKFpmyCs
XG4d2yYyEQZBzIvKOgLN+JDveiVoaXyqedVYOkTrmCRqutrfNVHr6xMFBhh9QD/qNQuGLvq72d03
3Jy2CtGCf0rca/tp+N4BXqsflKquRr0L2sjmuClOu+/8/NKvTQsNZ3l9ZqxeTew//1a6EA==
"""
)

# file activate.xsh
ACTIVATE_XSH = _convert(
    """
eJyNU11PwjAUfe+vuNY9sIj7ASQ+YCSBRD6i02gIaSq7gyWjXdqyaIz/3XYwVmB+9GFZ78c57T2n
lNIXKfQa+NJkJTcIeqmywkAqFZSZMlueoygppSRVcgPvrjgyUuYask0hlYEVGqaxAK6B7f8JSTAF
lmCN2uFqpcMeAbuyFGjxkcglhUwAzzOuUe9SbiWY18H5vm5B6sbgM4qir8jSdCib3t+x59FD/NS/
Z7N+PKRdoDRskAIXhBsIziqPyFrSf9O9xsPpZDgdD85JD6lz6kPqtwM0RYdx1bnB5Lka2u5cxzML
vKLWTjZ7mI5n8b8A9rUNjpAiQW3U1gmKFIQ0lXpW1gblEh4xT6EuvGjXtHGFE5ZcwlZotGhKYY4l
FwZKrjL+lqMmvoXmp4dYhKQV1M7d6yPEv5jNKcqYf1VGbcmZB5x4lRcCfzfvLXaBiCdJ5wj46uD+
Tmg3luR2NGGT/nhgGbpgX48wN7HaYhcUFjlfYrULCTkxWru36jF59rJ9NlJlf7JQde5j11VS+yZr
0d22eUPaxdycLKMTvqWjR3610emDtgTu36ylcJe83rhv/di/AYN1UZY=
"""
)

# file activate.bat
ACTIVATE_BAT = _convert(
    """
eJyVk1FLhEAUhd8X/A8XWSkf28dCyMUpBR3FzAiCS+WYwq4TOdXfb0Z3dTJdyCfveO85n8frNXut
OPCyNFbGqmUCzDxIs3s3REJzB1GrEE3VVJdQsLJuWAEYh97QkaRxlGRwbqxAXp1Uf+RYM32W1LKB
7Vp2nJC6DReD9m+5qeQ6Wd+a/SN7dlzn9oI7dxsSXJCcoXOskfLgYXdv/j8LnXiM8iGg/RmiZmOr
bFMSgcebMwGfKhgbBIfnL14X8P7BX3Zs38J3LSoQFdtD3YCVuJlvnfgmj5kfUz+OCLxxqUWoF9zk
qtYAFyZkBsO9ArzUh/td0ZqP9IskElTFMsnwb4/GqeoLPUlZT5dJvf8Id5hQIONynUSa2G0Wc+m8
Z+w2w4/Tt2hbYT0hbgOK1I0I4tUw/QOTZfLE
"""
)

# file deactivate.bat
DEACTIVATE_BAT = _convert(
    """
eJyFkN0KgkAUhO8X9h0GQapXCIQEDQX/EBO6kso1F9KN3Or1201Si6JzN+fMGT5mxQ61gKgqSijp
mETup9nGDgo3yi29S90QjmhnEteOYb6AFNjdBC9xvoj9iTUd7lzWkDVrwFuYiZ15JiW8QiskSlbx
lpUo4sApXtlJGodJhqNQWW7k+Ou831ACNZrC6BeW+eXPNEbfl7OiXr6H/oHZZl4ceXHoToG0nuIM
pk+k4fAba/wd0Pr4P2CqyLeOlJ4iKfkJo6v/iaH9YzfPMEoeMG2RUA==
"""
)

# file activate.ps1
ACTIVATE_PS = _convert(
    """
eJytVU1v4jAQvftXTNNoF9QNvSP1kG6RikQpIiyX3ZXlJkOx5NiR46RFK/77Oh+QkEBVrXYOSPZ8
+L2ZN8FNQ80TM149TgO68FePcAduvOMyVyEzXMlRvAtVHDMZjRJmtsStE+79YEIfpksbHySCG29h
vTBYYqpEjtXJcY9lb0cjZwj2WqM0hGwyGRbV4VWoFybGETJ7zpnBwc/0jZtw+xvcuZIPmBqdFS4c
wh8C1vgGBit7XT2RM83Zi8AxfZ490PV0ufrhz8oXD/GFuSjz8YHd5ZRj/BJjZUms60hweqEOeEGo
EqwJlJl7cgbggemYKhHRnGuTMUETreLEnEA8Bla+AulHuV2sU4Nx89ivSxktjGVTDpwm83UbTbto
Jwy8idZK+9X8Ai7sQMXuu5KGywy7j1xdmGJh1xCg2EBUe68+ptRI5OO4ZBepsIax7yutdNcgkp3Z
Wo8XQ3XrMv2aFknXkMkUDXCtUWDOpDkKLSUNEPCkklFDjhC33Sg7wcOWkG6zC2frSMgc3xq9nWgL
vDmLEXoSBBsvMmzETUhb5073yVtK76dzOvefJtRaEUaDyYJSB25aRaqpdXIth8C/n03oYvn8tFgd
ptht7hnVtebtOPVYTvV+Lumutw+NpBzatKFEUzDwpN1Sp62u3uC7cCoJ+lEEZosQZqlRVggaN/wd
jCov8Z2nVtav0Nm5koANzbnK0hozzctp3MGXTy5uYefJ3FwoPjzm7ludRJHiv/FmHbphpovPc832
G7xkBiIlv9pfnoZMR8DN6P83wZX41s13Bu6g/cfS2x9vhmwDwyE4pw3tF/t8N/fkLzQ3ME8=
"""
)

# file activate_this.py
ACTIVATE_THIS = _convert(
    """
eJylVE1v2zAMvetXENqh9pZ5wHYL0EMOBdqh64It7RAEhaE4TKzOlgxJ+ULR/15Sdhr341BsOcSW
9fj4SD5JSjkqgt6ogLDRLqxVhWYDS+ugWDuHJoA2AV3jkP6HQlx7BNxhkdgGTRJK7fOlrjDNHKpF
kg7g/iSPX/L8ZAhP+w9pJsSEVlAoA3OEtccFbEs0sLdrqNc+8CegTdxpH7RZwXgfSmv6+QdgbCDS
Z1rn2nxpIjQTUkqh68a6ANYf3rwO+PS+90IEtx8KoN9BqcBdgU2AK1XjmXPWtdtOaZI08h5d0NbE
nURO+3r/qRWpTIX4AFQTBS64AAgWxqPJOUQaYBjQUxuvFxgLZtBCOyyCdftU0DKnJZxSnVmjQpnR
ypD85LBWc8/P5CAhTQVtUcO0s2YmOZu8PcZ7bLI7q00y66hv4RMcA7IVhqQNGoCUaeabSofkGEz0
Yq6oI68VdYSx5m5uwIOjAp1elQHU3G5eVPhM683Fr8n16DI/u7qJkjkPk6nFom8G6AJqcq2PU//c
qOKvWiG3l4GlpbE1na1aQ9RYlMpoX4uL3/l4Op4Sf6m8CsElZBYqttk3+3yDzpMFcm2WlqZH2O/T
yfnPK0ITKmsqFejM1JkPygW/1dR4eac2irB6CU/w1lcsLe+k+V7DYv+5OMp6qefc6X4VnsiwaulY
6fvJXrN4bKOJ6s/Fyyrg9BTkVptvX2UEtSkJ18b8ZwkcfhTwXrKqJWuHd/+Q3T/IjLWqkHxk7f0B
pW9kFXTaNlwn+TjWSglSwaiMbMRP8l7yTAltE5AOc5VT8FLvDm2KC3F87VnyBzuZrUakdMERXe0P
7luSN+leWsYF5x/QAQdqeoHC4JZYKrr5+uq6t9mQXT/T8VrWHMRwmoqO9yGTUHF8YN/EHPbFI/bz
/no=
"""
)

def _write_file(dest, content, overwrite=True):
    if not dest.exists():
        with open(str(dest), "wb") as f:
            f.write(content.encode("utf-8"))
        return

def install_activate(creator):
    if IS_WIN:
        files = {"activate.bat": ACTIVATE_BAT, "deactivate.bat": DEACTIVATE_BAT, "activate.ps1": ACTIVATE_PS}

        # MSYS needs paths of the form /c/path/to/file
        drive, tail = os.path.splitdrive(str(creator.env_dir).replace(os.sep, "/"))
        home_dir_msys = (drive and "/{}{}" or "{}{}").format(drive[:1], tail)

        # Run-time conditional enables (basic) Cygwin compatibility
        home_dir_sh = """$(if [ "$OSTYPE" "==" "cygwin" ]; then cygpath -u '{}'; else echo '{}'; fi;)""".format(
            str(creator.env_dir), home_dir_msys
        )
        files["activate"] = ACTIVATE_SH.replace("__VIRTUAL_ENV__", home_dir_sh)
    else:
        files = {
            "activate": ACTIVATE_SH,
            "activate.fish": ACTIVATE_FISH,
            "activate.csh": ACTIVATE_CSH,
            "activate.ps1": ACTIVATE_PS,
        }
        files["activate_this.py"] = ACTIVATE_THIS

    if sys.version_info >= (3, 4):
        # Add xonsh support
        files["activate.xsh"] = ACTIVATE_XSH

    for name, content in files.items():
        content = content.replace("__VIRTUAL_PROMPT__", str(creator.prompt))
        content = content.replace("__VIRTUAL_WINPROMPT__", str(creator.prompt))
        content = content.replace("__VIRTUAL_ENV__", str(creator.env_dir))
        content = content.replace("__VIRTUAL_NAME__", str(creator.env_name))
        content = content.replace("__BIN_NAME__", str(creator.bin_name))
        content = content.replace("__PATH_SEP__", os.pathsep)
        _write_file(creator.bin_dir / name, content)