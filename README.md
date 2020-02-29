# CloudMitigator Semantic 
![Test and Release Version](https://github.com/cloudmitigator/semantic/workflows/Test%20and%20Release%20Version/badge.svg) [![PyPI version](https://badge.fury.io/py/cloudmitigator-semantic.svg)](https://badge.fury.io/py/cloudmitigator-semantic)


Allows you to manage versioning and releases using git tags as the source of truth. No more manual bumping
of version files. CloudMitigator Semantic allows the user to control releases via commit messages. All the rest is handled for you.
Just use trigger words listed below, and if a word is detected, a release will be automatically completed. Incrementing the specified number.

- Major release: `Major:` `major:`
- Minor release: `Minor:` `minor:`
- Patch release: `Patch:` `patch:`

Trigger words can also be modified through the inclusion of a semantic.yml.

    major:
      - "major:"
      - "breaking:"

    minor:
      - "minor:"

    patch:
      - "patch:"


## Installation:

Run `pip install cloudmitigator_semantic`
 
This will install a script called `semantic`

## Usage:

Run `semantic --help` for a list of commands that can be run. 

`semantic version` will return the latest git tag version if it has been changed, or the current git tag version if unchanged.

    v0.0.1
    
`semantic changed` will return a boolean on whether or not the version has been incremented.

    False
    

### Requirements:

Must run command within a directory that has git initialized.

If no version tag is specified then a default of v0.0.0 will be given. Make sure to tag your repo if you wish to start at a different seed number.

This module is only compatible with 'v' tagging. This means '0.0.0' will not be recognized where 'v0.0.1' will be.

This is meant to be run as part of a github action. Please see the sample implementation for an example.
