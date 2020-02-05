import logging
import os
import sys
import cloudmitigator_semantic.utilities
import cloudmitigator_semantic.version
import yaml


class GitActions:

    def __init__(self):
        self.git_commit_message = self.get_most_recent_commit_message()
        self.bump_type = self.scan_git_for_trigger_words()
        self.version = self.get_current_git_version_from_tag()
        self.check_if_bump_version()

    @staticmethod
    def get_current_git_version_from_tag():
        git_tag_list = cloudmitigator_semantic.utilities.run_bash_command_return_error("git tag")
        try:
            most_recent_tag = git_tag_list[-1]
        except IndexError as e:
            logging.error(f"No tags exist for current git repo, initializing at v0.0.0 {e}")
            most_recent_tag = "v0.0.0"
        return cloudmitigator_semantic.version.Version(most_recent_tag)

    @staticmethod
    def get_most_recent_commit_message():
        git_recent_commit = cloudmitigator_semantic.utilities.run_bash_command_return_error(
            "git log -1")
        git_recent_commit_message = git_recent_commit[-1]
        return git_recent_commit_message

    def scan_git_for_trigger_words(self):
        if os.path.exists("semantic.yml"):
            with open("semantic.yml") as trigger_file:
                trigger_dict = yaml.safe_load(trigger_file)
        else:
            trigger_dict = {
                "major": ["Major:", "major:", "Breaking:", "breaking:"],
                "minor": ["Minor:", "minor:"],
                "patch": ["Patch:", "patch:"],
                "prerelease": [],
                "metadata": []
            }
        message = self.get_most_recent_commit_message()
        for key in trigger_dict:
            for trigger_word in trigger_dict[key]:
                if trigger_word in message:
                    return key
        return None

    def check_if_bump_version(self):
        git_version = self.version
        bump_type = self.bump_type
        if bump_type is not None:
            if bump_type == "major":
                git_version.bump_major()
            if bump_type == "minor":
                git_version.bump_minor()
            if bump_type == "patch":
                git_version.bump_patch()

    def determine_if_bump_has_occurred(self):
        sys.stdout.write(f"{str(self.version.version_changed)} {str(self.version.version)}")

    def tag_current_repo(self):
        if self.version.version_changed:
            cloudmitigator_semantic.utilities.run_bash_command_return_error(
                f"git tag {self.version.version}"
            )


if __name__ == "__main__":
    git_actions = GitActions()
    sys.stdout.write(git_actions.version.version_changed)
    git_actions.tag_current_repo()
