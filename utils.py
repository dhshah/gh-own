"""Utility functions for the project."""
import subprocess
from pathlib import Path


def get_git_root():
    """Get the root of the git repository."""

    if not hasattr(get_git_root, "git_root"):
        get_git_root.git_root = None

    if get_git_root.git_root is None:
        # git rev-parse --show-toplevel
        get_git_root.git_root = (
            subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
            .decode("utf-8")
            .strip()
        )
    return get_git_root.git_root


def get_codeowners_file():
    """Get the codeowners file.

    Check if file exists in ${GIT_ROOT}/CODEOWNERS, ${GIT_ROOT}/.github/CODEOWNERS, or ${GIT_ROOT}/docs/CODEOWNERS.
    and return the first one found.
    """

    if not hasattr(get_codeowners_file, "codeowners_file"):
        get_codeowners_file.codeowners_file = None

    if get_codeowners_file.codeowners_file is None:
        git_root = get_git_root()

        get_codeowners_file.codeowners_file = f"{git_root}/CODEOWNERS"
        if Path(get_codeowners_file.codeowners_file).is_file():
            return get_codeowners_file.codeowners_file

        get_codeowners_file.codeowners_file = f"{git_root}/.github/CODEOWNERS"
        if Path(get_codeowners_file.codeowners_file).is_file():
            return get_codeowners_file.codeowners_file

        get_codeowners_file.codeowners_file = f"{git_root}/docs/CODEOWNERS"
        if Path(get_codeowners_file.codeowners_file).is_file():
            return get_codeowners_file.codeowners_file

        raise FileNotFoundError("CODEOWNERS file not found.")

    return get_codeowners_file.codeowners_file
