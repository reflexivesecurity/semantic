"""Handle interaction with bash."""
import subprocess


def run_bash_command_return_error(command):
    """Convert command into bash command."""
    command = command.split(" ")
    try:
        bash_return = subprocess.run(command, capture_output=True, check=True)
    except Exception as error:
        raise TypeError(
            f"Bash command did not execute properly"
            f" \n command: {command} \n error: {error}"
        )
    return bash_return.stdout.decode("utf-8")


def run_bash_command_split_lines_return_error(command):
    """Convert command into bash command split lines."""
    command = command.split(" ")
    try:
        bash_return = subprocess.run(command, capture_output=True, check=True)
    except Exception as error:
        raise TypeError(
            f"Bash command did not execute properly"
            f" \n command: {command} \n error: {error}"
        )
    return bash_return.stdout.decode("utf-8").splitlines()
