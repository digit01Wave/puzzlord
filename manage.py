#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def _prevent_failure_if_git_is_not_available() -> None:
    if os.environ.get("GIT_PYTHON_REFRESH") is None:
        os.environ["GIT_PYTHON_REFRESH"] = "quiet"


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    _prevent_failure_if_git_is_not_available()
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
