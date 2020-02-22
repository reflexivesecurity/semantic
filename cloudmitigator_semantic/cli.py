"""Handle cli interaction."""
import sys
import click
import cloudmitigator_semantic.git

GIT_ACTIONS = cloudmitigator_semantic.git.GitActions()


@click.group()
def semantic():
    """Instantiate click group."""
    pass


@semantic.command(
    "changed",
    short_help="Return the latest git tag version if it has been "
    "changed, or the current git tag version if unchanged.",
)
def changed():
    """Click command to check if repo version changed."""
    sys.stdout.write(str(GIT_ACTIONS.version.version_changed))


@semantic.command(
    "version",
    short_help="Return a boolean on whether or not the version has been "
    "incremented.",
)
def version():
    """Click command to return current/new version."""
    sys.stdout.write(str(GIT_ACTIONS.version.version))


if __name__ == "__main__":
    semantic()
