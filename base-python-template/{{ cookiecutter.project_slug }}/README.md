# {{ cookiecutter.__import_slug }}

{{ cookiecutter.project_short_description }}


## Installation

{% if cookiecutter.remote_git_dir == '' -%}

{% if cookiecutter.remote_git_private == 'Yes' -%}
```shell
pip install 'git+ssh://git@{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git'
```
{% else -%}
```shell
pip install 'git+https://{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git'
```
{% endif -%}

{% else -%}
{% if cookiecutter.remote_git_private == 'Yes' -%}
```shell
pip install '{{ cookiecutter.project_slug }} @ git+ssh://git@{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git@{{ cookiecutter.remote_git_branch }}#subdirectory={{ cookiecutter.remote_git_dir }}' 
```
{% else -%}
```shell
pip install '{{ cookiecutter.project_slug }} @ git+https://{{ cookiecutter.remote_git_url }}/{{ cookiecutter.remote_git_repo }}.git@{{ cookiecutter.remote_git_branch }}#subdirectory={{ cookiecutter.remote_git_dir }}' 
```
{% endif -%}
{% endif %}


## Usage

```python
import {{ cookiecutter.__import_slug }}

print({{ cookiecutter.__import_slug }}.__version__)
```


## License

`{{ cookiecutter.project_slug }}` was created by {{ cookiecutter.__creator }}.

`{{ cookiecutter.project_slug }}` is owned by {{ cookiecutter.__owner }}.

`{{ cookiecutter.project_slug }}` is licensed under the terms of {{ cookiecutter.project_license }} license
(see `LICENSE` file for details.)

{% if cookiecutter.project_license == 'None' or cookiecutter.project_license == 'Proprietary' -%}
{{ cookiecutter.__owner }} retains all rights to the source, and it may not be reproduced, distributed, 
or used to create derivative works without explicit permission.
{% endif -%}
