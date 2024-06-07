PACKAGE_NAME = "{{ cookiecutter.project_slug }}"
PYTHON = python3
PIP = pip

all:
	@echo "Please specify target"

build:
	$(PIP) install --upgrade setuptools
	$(PIP) install --upgrade build
	$(PYTHON) -m build

install:
	$(PIP) install .

install-edit:
	$(PIP) install -e .

#install-wheel: build
#	(cd dist/ && $(PIP) install $(PACKAGE_NAME).whl)
#
#install-dist: build
#	(cd dist/ && tar xzf $(PACKAGE_NAME).tar.gz && $(PIP) install $(PACKAGE_NAME)/)

install-git:
	{% if cookiecutter.remote_git_dir == '' -%}
	{% if cookiecutter.remote_git_private == 'Yes' -%}
	$(PIP) install 'git+ssh://git@{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git'
	{% else -%}
	$(PIP) install 'git+https://{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git'
	{% endif -%}
	{% else -%}
	{% if cookiecutter.remote_git_private == 'Yes' -%}
	$(PIP) install '{{ cookiecutter.project_slug }} @ git+ssh://git@{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git@{{ cookiecutter.remote_git_branch }}#subdirectory={{ cookiecutter.remote_git_dir }}'
	{% else -%}
	$(PIP) install '{{ cookiecutter.project_slug }} @ git+https://{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git@{{ cookiecutter.remote_git_branch }}#subdirectory={{ cookiecutter.remote_git_dir }}'
	{% endif -%}
	{% endif %}


.PHONY: all build install install-edit install-git  # install-dist install-wheel
