"""pymqpcf package."""

from importlib.metadata import version as _version

__all__ = ["get_version"]


def get_version() -> str:
    """Return the installed package version."""
    return _version("pymqpcf")
