import importlib.metadata
import logging
import pathlib


__version__ = importlib.metadata.version("{{ cookiecutter.__project_dash }}")
""" Package version -- read only value """


__version_tuple__ = tuple(__version__.split('.'))
""" Package version tuple -- read only value """


__package_root__ = pathlib.Path(__file__).parent.parent
""" Path of package root in filesystem -- read only value """


__package_logger_name__ = "{{ cookiecutter.__import_slug }}"
""" Name of default package logger -- read only value """


__package_default_log_level__ = logging.WARNING
""" Default log level for package logger -- read only value """
