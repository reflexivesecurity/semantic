"""Object handling interactions between the command line and git."""

import os
import re
import yaml
import cloudmitigator_semantic.utilities
import cloudmitigator_semantic.version


class GitActions:
    """Object holding all git actions."""

    def __init__(self):
        """Call object methods to instantiate shared features."""
        self.git_commit_message = self.get_most_recent_commit_message()
        self.bump_type = self.scan_git_for_trigger_words()
        self.version = self.get_current_git_version_from_tag()
        self.check_if_bump_version()

    @staticmethod
    def get_current_git_version_from_tag():
        """
        Get list of all current git tags, and return the most recent one.

        :return: Version object initialized with current tag.
        """
        git_tag_list = cloudmitigator_semantic.utilities. \
            run_bash_command_split_lines_return_error(
                "git tag -l --sort=-v:refname"
            )
        regex = (
            r"^v(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch"
            r">0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-]"
            r"[0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]"
            r"*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA"
            r"-Z-]+)*))?$"
        )
        most_recent_tag = "v0.0.0"
        for tag in git_tag_list:
            if re.search(regex, tag):
                most_recent_tag = tag
                break
        return cloudmitigator_semantic.version.Version(most_recent_tag)

    @staticmethod
    def get_most_recent_commit_message():
        """Extract git commit message from git log commands."""
        git_recent_commit = cloudmitigator_semantic.utilities. \
            run_bash_command_return_error(
                "git log -1"
            )
        return git_recent_commit.lower()

    def scan_git_for_trigger_words(self):
        """Check if trigger word in commit message."""
        if os.path.exists(f"{os.getcwd()}/semantic.yml"):
            with open(f"{os.getcwd()}/semantic.yml") as trigger_file:
                trigger_dict = yaml.safe_load(trigger_file)
        else:
            trigger_dict = {
                "major": ["major:", "breaking:"],
                "minor": ["minor:"],
                "patch": ["patch:"],
                "prerelease": [],
                "metadata": [],
            }
        message = self.git_commit_message
        for key in trigger_dict:
            for trigger_word in trigger_dict[key]:
                if trigger_word in message:
                    return key
        return None

    def check_if_bump_version(self):
        """Check if version bump trigger word detected."""
        git_version = self.version
        bump_type = self.bump_type
        if bump_type is not None:
            if bump_type == "major":
                git_version.bump_major()
            elif bump_type == "minor":
                git_version.bump_minor()
            elif bump_type == "patch":
                git_version.bump_patch()

    def tag_current_repo(self):
        """Tag git repo with updated version."""
        if self.version.version_changed:
            cloudmitigator_semantic.utilities.run_bash_command_return_error(
                f"git tag {self.version.version}"
            )

    def get_commits_between_tags(self):
        """Create release body for Github Actions"""
        release_body = cloudmitigator_semantic.utilities. \
            run_bash_command_return_error(
                f"git log {self.version.original_version}..HEAD "
                f"--pretty=format:%s</br>"
            )
        return release_body
