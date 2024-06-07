import json
import os
import pathlib
import shutil
import sys
import tomllib


##############################################################################
# Utilities
##############################################################################


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def copy(from_file, to_file):
    shutil.copy(from_file, to_file)


def move(from_file, to_file):
    shutil.move(from_file, to_file)


def parse_python_version(version: str, default: str) -> str:
    start = next((i for i, c in enumerate(version) if c in "0123456789."), len(version))
    end = next((j for j, c in reversed(list(enumerate(version))) if c in "0123456789."), len(version)-1) + 1
    return version[start:end] if start < end else default


class SwitchSysPath:
    def __init__(self, newpath: list):
        self.syspath = newpath

    def switch(self) -> None:
        sys.path, self.syspath = self.syspath, sys.path

    def __enter__(self):
        self.switch()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.switch()


class SuppressExceptionsAndWarn:
    def __init__(self, prompt=None):
        self.prompt = prompt

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            print(f'warning: {self.prompt}: exception `{exc_val}` raised and ignored. '
                  f'may affect behavior',
                  file=sys.stderr
                  )
        return True


##############################################################################
# Cookiecutter clean-up
##############################################################################


# Directive flags
no_license = "{{cookiecutter.project_license}}" == "None"
has_gitignore = "{{cookiecutter.add_project_gitignore}}" == "Yes"


# Remove license (if specified)
with SuppressExceptionsAndWarn('remove license file'):
    if no_license:
        remove("LICENSE")


# Remove gitignore (if specified)
with SuppressExceptionsAndWarn('setting up gitignore file'):
    if has_gitignore:
        copy("dotgitignore", ".gitignore")
        remove("dotgitignore")
    else:
        remove("dotgitignore")


# Remove namespace package if not a namespace lib
namespace = "{{ cookiecutter.namespace }}"
namespace = namespace.strip()
if namespace:
    move("src/{{ cookiecutter.namespace_slug }}__", "src/{{ cookiecutter.namespace_slug }}")
    remove("src/{{ cookiecutter.package_slug }}/")
else:
    remove("src/{{ cookiecutter.namespace_slug }}__/")


# Create requirements.txt and environment.yml files
try:
    with SwitchSysPath([os.getcwd(), *sys.path]):
        import scripts.pyproject_to_requirements  # noqa
        scripts.pyproject_to_requirements.main(['--pyproject=pyproject.toml', '--all', '--output-dir=.'])
except BaseException as e:
    if not isinstance(e, SystemExit) or e.code != 0:
        print(f"warning: exception `{e}` raised while writing requirements files.", file=sys.stderr)


# Create cookiecutter-replay.json
with SuppressExceptionsAndWarn('writing cookiecutter replay file'):
    cookiecutter_context = json.loads("""{{ cookiecutter | jsonify }}""")

    cookiecutter_template = {}
    if 'COOKIECUTTER_TEMPLATE_HOME' in os.environ:
        template_base = cookiecutter_context['_template']
        template_root = pathlib.Path(os.environ['COOKIECUTTER_TEMPLATE_HOME'])
        template_path = template_root / template_base
        template_file = template_path / 'cookiecutter.json'
        with SuppressExceptionsAndWarn("reading cookiecutter.json file"):
            with open(template_file, 'r') as fd:
                cookiecutter_template = json.load(fd)

    cookiecutter_context.pop('_checkout', None)
    cookiecutter_context.pop('_output_dir', None)
    cookiecutter_context.pop('_repo_dir', None)
    cookiecutter_context.pop('_template', None)

    with open("cookiecutter-replay.json", "w") as fd:
        cookiecutter_replay = {"cookiecutter": cookiecutter_context, "_cookiecutter": cookiecutter_template}
        json.dump(cookiecutter_replay, fd, indent=2, ensure_ascii=False)


sys.exit(0)
