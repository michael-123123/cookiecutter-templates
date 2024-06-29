# {{ cookiecutter.__import_slug }}

{{ cookiecutter.project_short_description }}


## Installation



## Usage

```python
import {{ cookiecutter.__import_slug }}

print({{ cookiecutter.__import_slug }}.__version__)
```


## License

`{{ cookiecutter.__project_dash }}` was created by {{ cookiecutter.__creator }}.

`{{ cookiecutter.__project_dash }}` is owned by {{ cookiecutter.__owner }}.

`{{ cookiecutter.__project_dash }}` is licensed under the terms of {{ cookiecutter.project_license }} license
(see `LICENSE` file for details.)

{% if cookiecutter.project_license == 'None' or cookiecutter.project_license == 'Proprietary' -%}
{{ cookiecutter.__owner }} retains all rights to the source, and it may not be reproduced, distributed, 
or used to create derivative works without explicit permission.
{% endif -%}
