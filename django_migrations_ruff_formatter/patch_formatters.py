"""
django.core.management.utils.find_formatters and .utils.run_formatters are
patched to use ruff for formatting Django generated files, instead of black.

These patches are applied when they are imported from core.__init__ during the Django startup.
"""

import shutil
import subprocess  # noqa: S404
import sys
import traceback

from django.conf import settings
from django.core.management import utils


def find_formatters() -> dict:
    """
    Find the ruff executable.
    """
    return {"ruff_path": shutil.which("ruff")}


utils.find_formatters = find_formatters


def run_formatters(written_files, ruff_path=(sentinel := object()), stderr=sys.stderr):  # noqa: B008
    """
    Run ruff on the given files.
    """
    # Use a sentinel rather than None, as which() returns None when not found.
    if ruff_path is sentinel:
        ruff_path = shutil.which("ruff")

    if ruff_path:
        extra_lint_args = getattr(settings, "RUFF_EXTRA_LINT_ARGS", [])
        lint_args = [ruff_path, "check", "--fix", *extra_lint_args, *written_files]
        extra_format_args = getattr(settings, "RUFF_EXTRA_FORMAT_ARGS", [])
        format_args = [ruff_path, "format", *extra_format_args, *written_files]
        try:
            subprocess.run(lint_args, capture_output=True)
            print(f"{format_args=}")
            subprocess.run(format_args, capture_output=True)
        except OSError:
            stderr.write("Formatters failed to launch:")
            traceback.print_exc(file=stderr)


utils.run_formatters = run_formatters
