class FS:
    """
    Responsible for handling the file system logic. All requests coming from FUSE
    are forwarded to an instance of this class. Values returned by its methods
    are compatible with values expected by FUSE Python bindings. In case of
    errors negative integers are returned
    """

    def __init__(self, swift):
        """
        An FS instance is created when a file system is mounted. The first
        argument should be a cumulonimbus.swift.Swift instance.
        """
        self.swift = swift
        pass

    def opendir(self, path):
        """
        Called when a directory is opened. Returns None.
        """
        self.swift.get(path)

    def releasedir(self, path, dh):
        """
        Closes a directory opened with opendir.
        """
        assert(dh is None)

    def readdir(self, path, offset, dh):
        """
        Yields fuse.Direntry instances representing objects in the given
        directory.
        """
        assert(dh is None)

    def create(self, path, mode, rdev):
        """
        Creates a new file with a given mode and returns None.
        """
        pass

    def write(self, path, buf, offset, fh):
        """
        Writes contents of buf to file at path beginning at the given offset.
        Returns the number of successfully written bytes.
        """
        assert(fh is None)
