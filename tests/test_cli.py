import unittest
from click.testing import CliRunner
from cloudmitigator_semantic import cli
from cloudmitigator_semantic import git


class CliTestCase(unittest.TestCase):

    def test_semantic_cli_call(self):
        runner = CliRunner()
        test = runner.invoke(cli.semantic)
        self.assertEqual(test.exit_code, 0)

    def test_version_cli_call(self):
        git_actions = git.GitActions()
        runner = CliRunner()
        test = runner.invoke(cli.version)
        self.assertEqual(test.output, git_actions.version.version)

    def test_version_changed_cli_call(self):
        git_actions = git.GitActions()
        runner = CliRunner()
        test = runner.invoke(cli.changed)
        self.assertEqual(test.output, str(git_actions.version.version_changed))
