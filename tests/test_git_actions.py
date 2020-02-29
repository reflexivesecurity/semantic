import unittest
from unittest.mock import patch

from cloudmitigator_semantic import git


class GitActionsTestCase(unittest.TestCase):

    @patch('cloudmitigator_semantic.utilities.run_bash_command_split_lines_return_error')
    def test_git_actions_with_semantic_yml_matching_trigger_word_patch(self, mock_bash):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = ["patch: ", ["v1.0.1"]]
            mock_bash.side_effect = [["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.0.2")

    @patch('os.path.exists')
    @patch('cloudmitigator_semantic.utilities.run_bash_command_split_lines_return_error')
    def test_git_actions_with_out_semantic_yml_matching_trigger_word_patch(self, mock_bash, mock_os):
        mock_os.side_effect = [False]
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = ["patch: ", ["v1.0.1"]]
            mock_bash.side_effect = [["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.0.2")

    @patch('cloudmitigator_semantic.utilities.run_bash_command_split_lines_return_error')
    def test_git_actions_with_semantic_yml_no_matching_trigger_word(self, mock_bash):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = ["best", ["v1.0.1"]]
            mock_bash.side_effect = [["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.0.1")

    @patch('cloudmitigator_semantic.utilities.run_bash_command_split_lines_return_error')
    def test_git_actions_with_semantic_yml_no_git_version(self, mock_bash):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = ["best", []]
            mock_bash.side_effect = [[]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v0.0.0")

    @patch('cloudmitigator_semantic.utilities.run_bash_command_split_lines_return_error')
    def test_git_actions_with_semantic_yml_matching_trigger_word_major(self, mock_bash):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = ["major: ", ["v1.0.1"]]
            mock_bash.side_effect = [["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v2.0.0")

    @patch('cloudmitigator_semantic.utilities.run_bash_command_split_lines_return_error')
    def test_git_actions_with_semantic_yml_matching_trigger_word_minor(self, mock_bash):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = ["minor: ", ["v1.0.1"]]
            mock_bash.side_effect = [["v1.0.1"]]
            git_actions = git.GitActions()
            self.assertEqual(git_actions.version.version, "v1.1.0")

    @patch('cloudmitigator_semantic.utilities.run_bash_command_split_lines_return_error')
    def test_git_actions_tag_current_repo(self, mock_bash):
        with patch(
                'cloudmitigator_semantic.utilities.run_bash_command_return_error') as version_patch:
            version_patch.side_effect = ["minor: ", "none"]
            mock_bash.side_effect = [["v1.0.1"]]
            git_actions = git.GitActions()
            git_actions.tag_current_repo()
            version_patch.assert_called_with("git tag v1.1.0")

