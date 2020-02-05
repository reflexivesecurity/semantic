import sys

import click
import cloudmitigator_semantic.git

git_actions = cloudmitigator_semantic.git.GitActions()


@click.group()
def semantic():
    pass


@semantic.command("version-changed")
def version_changed():
    sys.stdout.write(str(git_actions.version.version_changed))


@semantic.command("version")
def version():
    sys.stdout.write(str(git_actions.version))


if __name__ == "__main__":
    semantic()
