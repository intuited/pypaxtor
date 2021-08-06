## pypaxtor: Package Storage provisioning

Simple module that provides a path to a storage location
under the user home directory in a cross-platform manner.

Under MacOS this will be in `~/Library/Application Support`;
under Windows it will be in `$HOME/AppData/Local`;
and under Linux it will be in `~/.local/share`.

Packages using this module supply a package name when requesting a storage location.
A directory with that name is created under the directory named `PyPaxtor`
in the os-appropriate location.

### Usage:

    >>> import pypaxtor
    >>> savedir = pypaxtor.get_storage_location('my_package')
    >>> savedir  # if on Mac as user `rlyacht`
    PosixPath('/Users/rlyacht/Library/Application Support/pypaxtor/my_package')
    >>> with open(savedir / 'SaveFile.txt') as savefile:
    ...     # do stuff

If the above code is executed on a linux system,
the saved file will be located at `/home/rlyacht/.local/share/pypaxtor/my_package/SaveFile.txt`.
