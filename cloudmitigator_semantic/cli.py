import sys

import click
import cloudmitigator_semantic.git

git_actions = cloudmitigator_semantic.git.GitActions()


@click.group()
def semantic():
    pass


@semantic.command("changed", short_help="Return the latest git tag version if it has been "
                                        "changed, or the current git tag version if unchanged.")
def changed():
    sys.stdout.write(str(git_actions.version.version_changed))


@semantic.command("version", short_help="Return a boolean on whether or not the version has been "
                                        "incremented.")
def version():
    sys.stdout.write(str(git_actions.version.version))


if __name__ == "__main__":
    semantic()
