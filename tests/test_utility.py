import unittest

from cloudmitigator_semantic import utilities


class UtilityTestCase(unittest.TestCase):

    def test_bash_commands(self):
        command = "echo Hello"
        output = utilities.run_bash_command_return_error(command)
        self.assertEqual(output[0], "Hello")

    def test_bash_command_failure(self):
        with self.assertRaises(TypeError):
            command = "echo! Hello"
            output = utilities.run_bash_command_return_error(command)



