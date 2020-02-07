import re


class Version:

    def __init__(self, version):
        self.__version = version
        self.major = None
        self.minor = None
        self.patch = None
        self.prerelease = None
        self.metadata = None
        self.initialize_version_object()

    @property
    def version(self):
        base_version = f"v{str(self.major)}.{str(self.minor)}.{str(self.patch)}"
        if self.prerelease is not None:
            base_version = f"{base_version}-{self.prerelease}"
            if self.metadata is not None:
                base_version = f"{base_version}+{self.metadata}"
        return base_version

    @property
    def original_version(self):
        return self.__version

    @property
    def version_changed(self):
        if self.__version == self.version:
            return False
        return True

    def initialize_version_object(self):
        regex = r"^v(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
        version_match = re.search(regex, self.__version)
        if version_match.group("major"):
            self.major = int(version_match.group("major"))
        elif version_match.group("minor"):
            self.minor = int(version_match.group("minor"))
        elif version_match.group("patch"):
            self.patch = int(version_match.group("patch"))
        elif version_match.group("prerelease"):
            self.prerelease = version_match.group("prerelease")
        elif version_match.group("buildmetadata"):
            self.metadata = version_match.group("buildmetadata")

    def bump_minor(self):
        self.minor += 1
        self.patch = 0
        self.prerelease = None
        self.metadata = None

    def bump_major(self):
        self.major += 1
        self.minor = 0
        self.patch = 0
        self.prerelease = None
        self.metadata = None

    def bump_patch(self):
        self.patch += 1
        self.prerelease = None
        self.metadata = None

    def append_prerelease(self, prerelease):
        self.prerelease = prerelease

    def append_meta_data(self, metadata):
        self.metadata = metadata

