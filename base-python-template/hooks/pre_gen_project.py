import sys
from string import ascii_letters


# debug
# print(""" { {  cookiecutter | jsonify } } """)


# if package is empty - fail
project_dash = "{{ cookiecutter.__project_dash }}"
if not project_dash or project_dash[0] not in ascii_letters:
    print(f"error: invalid project name `{project_dash}`!", file=sys.stderr)
    sys.exit(1)


package_slug = "{{ cookiecutter.__package_slug }}"
if not package_slug or package_slug[0] not in ascii_letters:
    print(f"error: invalid package name `{package_slug}`!", file=sys.stderr)
    sys.exit(1)


sys.exit(0)
