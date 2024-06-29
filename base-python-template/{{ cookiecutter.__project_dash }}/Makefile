# Commands
PYTHON  = python
PIP    := $(PYTHON) -m pip
BUILD  := $(PYTHON) -m build
TWINE  := $(PYTHON) -m twine

# Repos
GIT_REPO        := "{{ cookiecutter.__remote_git_pip_install_path }}"
{% if cookiecutter.add_twine_support == 'Yes' -%}
TWINE_REPO_URL  := "{{ cookiecutter.twine_repository }}"
TWINE_REPO_ARG  := {{ cookiecutter.__twine_repository_url }}
TWINE_INDEX_ARG := {{ cookiecutter.__twine_pip_index_url }}
{% endif %}

# Package info
PACKAGE_NAME  = "{{ cookiecutter.__project_dash }}"
VERSION      := $(shell $(PYTHON) ./scripts/pyproject_version_manager.py --pyproject=pyproject.toml get)


# Targets


all: help


help:
	@echo "Please specify a target:"
	@echo "# TODO"


clean:
	rm -rf dist/* docs/_build/ src/*egg-info build/


build-tools:
	$(PIP) install --upgrade setuptools build

build: build-tools
	$(BUILD)


{% if cookiecutter.add_twine_support == 'Yes' -%}
twine-tools: build-tools
	$(PIP) install --upgrade twine

twine: twine-tools
	$(TWINE) upload --verbose $(TWINE_REPO_ARG) dist/*


{% else -%}


{% endif -%}


install-test:
	$(PIP) install .

install-dev:
	$(PIP) install -e .

install-latest:
	$(PIP) install $(GIT_REPO)

{% if cookiecutter.add_twine_support == 'Yes' -%}
install:
	$(PIP) install --upgrade $(TWINE_INDEX_ARG) $(PACKAGE_NAME)
{% else -%}
install: install-latest
{% endif %}


doc:
	(cd doc && make)

doc-%:
	(cd doc && make $*)



.PHONY: all help clean build-tools build twine-tools twine install-test install-dev install-latest install doc
