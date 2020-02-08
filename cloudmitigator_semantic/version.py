"""Object representation of a version."""

import re


class Version:
    """Class representing version."""

    def __init__(self, version):
        """
        Initialize version object with a semantic version starting with "v".

        :param version: string version eg. "v5.1.2"
        """
        self.__version = version
        self.major = None
        self.minor = None
        self.patch = None
        self.prerelease = None
        self.metadata = None
        self.initialize_version_object()

    @property
    def version(self):
        """
        Property that returns formatted version string.

        :return: string formatted version
        """
        base_version = f"v{str(self.major)}." f"" \
                       f"" f"{str(self.minor)}.{str(self.patch)}"
        if self.prerelease is not None:
            base_version = f"{base_version}-{self.prerelease}"
            if self.metadata is not None:
                base_version = f"{base_version}+{self.metadata}"
        return base_version

    @property
    def original_version(self):
        """
        Show the original version string.

        :return: original version string
        """
        return self.__version

    @property
    def version_changed(self):
        """
        Boolean representing if the version had been changed.

        :return: Boolean
        """
        if self.__version == self.version:
            return False
        return True

    def initialize_version_object(self):
        """Instantiate regex to look at version string, and parse it."""
        regex = (
            r"^v(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch"
            r">0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-]"
            r"[0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]"
            r"*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA"
            r"-Z-]+)*))?$"
        )

        version_match = re.search(regex, self.__version)
        if version_match.group("major"):
            self.major = int(version_match.group("major"))
        if version_match.group("minor"):
            self.minor = int(version_match.group("minor"))
        if version_match.group("patch"):
            self.patch = int(version_match.group("patch"))
        if version_match.group("prerelease"):
            self.prerelease = version_match.group("prerelease")
        if version_match.group("buildmetadata"):
            self.metadata = version_match.group("buildmetadata")

    def bump_minor(self):
        """Logic to bump a minor version."""
        self.minor += 1
        self.patch = 0
        self.prerelease = None
        self.metadata = None

    def bump_major(self):
        """Logic to bump a major version."""
        self.major += 1
        self.minor = 0
        self.patch = 0
        self.prerelease = None
        self.metadata = None

    def bump_patch(self):
        """Logic to bump a patch version."""
        self.patch += 1
        self.prerelease = None
        self.metadata = None

    def append_prerelease(self, prerelease):
        """Logic to add prerelease data."""
        self.prerelease = prerelease

    def append_meta_data(self, metadata):
        """Logic to add build metadata."""
        self.metadata = metadata
