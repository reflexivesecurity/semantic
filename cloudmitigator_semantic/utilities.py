import subprocess


def run_bash_command_return_error(command):
    command = command.split(" ")
    try:
        bash_return = subprocess.run(command, capture_output=True)
    except subprocess.CalledProcessError as e:
        raise TypeError(f"Bash command did not execute properly"
                        f" \n command: {command} \n error: {e}")
    return bash_return.stdout.decode("utf-8").splitlines()
