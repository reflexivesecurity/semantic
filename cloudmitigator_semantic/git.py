"""Object handling interactions between the command line and git."""

import logging
import os
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
        git_tag_list = cloudmitigator_semantic.utilities.\
            run_bash_command_return_error(
                "git tag"
            )
        try:
            most_recent_tag = git_tag_list[-1]
        except IndexError as error:
            logging.error(
                "No tags exist for current git"
                " repo initializing at v0.0.0 %s", error
            )
            most_recent_tag = "v0.0.0"
        return cloudmitigator_semantic.version.Version(most_recent_tag)

    @staticmethod
    def get_most_recent_commit_message():
        """Extract git commit message from git log commands."""
        git_recent_commit = cloudmitigator_semantic.utilities.\
            run_bash_command_return_error(
                "git log -1"
            )
        git_recent_commit_message = git_recent_commit[-1]
        return git_recent_commit_message

    def scan_git_for_trigger_words(self):
        """Check if trigger word in commit message."""
        if os.path.exists(f"{os.getcwd()}/semantic.yml"):
            with open(f"{os.getcwd()}/semantic.yml") as trigger_file:
                trigger_dict = yaml.safe_load(trigger_file)
        else:
            trigger_dict = {
                "major": ["Major:", "major:", "Breaking:", "breaking:"],
                "minor": ["Minor:", "minor:"],
                "patch": ["Patch:", "patch:"],
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
