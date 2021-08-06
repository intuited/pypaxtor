"""pypaxtor: Python Package Storage provisioning

Simple module that provides a path to a storage location
under the user home directory in a cross-platform manner.

Under MacOS this will be in `~/Library/Application Support`;
under Windows it will be in `$HOME/AppData/Local`;
and under Linux it will be in `~/.local/share`.

Packages using this module supply a package name when requesting a storage location.
A directory with that name is created under the directory named `PyPaxtor`
in the os-appropriate location.
"""
from pathlib import Path

class SystemStorageLocationNotFound(Exception):
    """Raised if pypaxtor is unable to find any of the system-specific storage paths."""

def get_storage_location(package_name):
    """Returns a Path to directory `package_name` in the appropriate location.

    Determines the appropriate storage directory based on the existence of
    the various storage locations used by different operating systems.

    If `package_name` does not exist in the appropriate directory,
    creates it.

    Returns a `pathlib.Path` object for the directory named after `package_name`.
    """
    home = Path.home()

    mac_storage = home / 'Library' / 'Application Support'
    lin_storage = home / '.local' / 'share'
    win_storage = home / 'AppData' / 'Local'

    for path in (mac_storage, lin_storage, win_storage):
        if path.is_dir():
            ret = path / 'pypaxtor' / package_name
            ret.mkdir(parents=True, exist_ok=True)
            return ret

    raise SystemStorageLocationNotFound(
            'pypaxtor was unable to find any standard storage location on your system.')
