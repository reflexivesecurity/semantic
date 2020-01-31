import logging
import sys
import cloudmitigator_semantic.utilities
import cloudmitigator_semantic.version

trigger_dict = {
    "major": ["Major:", "major:", "Breaking:", "breaking:"],
    "minor": ["Minor:", "minor:"],
    "patch": ["Patch:", "patch:"],
    "prerelease": [],
    "metadata": []
}


def get_current_git_version_from_tag():
    git_tag_list = cloudmitigator_semantic.utilities.run_bash_command_return_error("git tag")
    try:
        most_recent_tag = git_tag_list[-1]
    except IndexError as e:
        logging.error(f"No tags exist for current git repo, initializing at v0.0.0 {e}")
        most_recent_tag = "v0.0.0"
    return cloudmitigator_semantic.version.Version(most_recent_tag)


def get_most_recent_commit_message():
    git_recent_commit = cloudmitigator_semantic.utilities.run_bash_command_return_error(
        "git log -1")
    git_recent_commit_message = git_recent_commit[-1]
    return git_recent_commit_message


def scan_git_for_trigger_words():
    message = get_most_recent_commit_message()
    for key in trigger_dict:
        for trigger_word in trigger_dict[key]:
            if trigger_word in message:
                return key
    return None


def check_if_bump_version():
    git_version = get_current_git_version_from_tag()
    bump_type = scan_git_for_trigger_words()
    if bump_type is not None:
        if bump_type == "major":
            git_version.bump_major()
        if bump_type == "minor":
            git_version.bump_minor()
        if bump_type == "patch":
            git_version.bump_patch()
    return git_version


def determine_if_bump_has_occurred():
    git_version = check_if_bump_version()
    sys.stdout.write(f"{str(git_version.version_changed)} {str(git_version.version)}")
    return git_version.version_changed, git_version.version


if __name__ == "__main__":
    determine_if_bump_has_occurred()
