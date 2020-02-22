import unittest
from unittest.mock import patch

from cloudmitigator_semantic import git


class GitActionsTestCase(unittest.TestCase):

    def test_git_actions_with_semantic_yml_matching_trigger_word_patch(self):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = [["patch: "], ["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.0.2")

    @patch('os.path.exists')
    def test_git_actions_with_out_semantic_yml_matching_trigger_word_patch(self, mock_os):
        mock_os.side_effect = [False]
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = [["patch: "], ["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.0.2")

    def test_git_actions_with_semantic_yml_no_matching_trigger_word(self):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = [["best"], ["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.0.1")

    def test_git_actions_with_semantic_yml_no_git_version(self):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = [["best"], []]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v0.0.0")

    def test_git_actions_with_semantic_yml_matching_trigger_word_major(self):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = [["major: "], ["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v2.0.0")

    def test_git_actions_with_semantic_yml_matching_trigger_word_minor(self):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = [["minor: "], ["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.1.0")

    def test_git_actions_tag_current_repo(self):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = [["minor: "], ["v1.0.1"], "none"]
            git_actions = git.GitActions()
            git_actions.tag_current_repo()
            version_patch.assert_called_with("git tag v1.1.0")

