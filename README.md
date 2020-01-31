# CloudMitigator Semantic

Allows you to manage versioning and releases using git tags as the source of truth. No more manual bumping
of version files. CloudMitigator Semantic allows the user to control releases via commit messages. All the rest is handled for you.
Just use trigger words listed below, and if a word is detected, a release will be automatically completed. Incrementing the specified number.

- Major release: `Major:` `major:`
- Minor release: `Minor:` `minor:`
- Patch release: `Patch:` `patch:`

## Installation:

Run `pip install cloudmitigator_semantic`

This will install a script called `semantic`

## Usage:

Run `semantic` in the directory you wish to check. The script will print out a message that looks like.

    [True, 'v0.0.1']
    
or

    [False, 'v0.0.0']
    
The first part tells you whether a trigger word was found in the commit message.

The second part tells you what version it is currently (if False), or will become (if True)

### Requirements:

Must run command within a directory that has git initialized.

If no version tag is specified then a default of v0.0.0 will be given. Make sure to tag your repo if you wish to start at a different seed number.

This module is only compatible with 'v' tagging. This means '0.0.0' will not be recognized where 'v0.0.1' will be.
