import sys

# debug
# print(""" { {  cookiecutter | jsonify } } """)

# if package is empty - fail
if not "{{ cookiecutter.package_slug }}":
    print("error: cannot have empty package name!", file=sys.stderr)
    sys.exit(1)


# update remote git dir to default (if exists)
"""{% if cookiecutter.remote_git_dir == '-' %}
    {{ cookiecutter.update(
        {
            "remote_git_dir": cookiecutter.__default_lib_path + '/' + cookiecutter.project_slug,
        }
    )}}
    {% endif %}
"""

sys.exit(0)
