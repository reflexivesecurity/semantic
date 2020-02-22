import setuptools
import cloudmitigator_semantic.git
from os import path

git_actions = cloudmitigator_semantic.git.GitActions()

requirements_files = ['requirements.txt']

install_requires = []

for requirements_file in requirements_files:
    with open(requirements_file, 'r') as f:
        install_requires += f.readlines()

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='cloudmitigator_semantic',
                 version=git_actions.version.version,
                 description='Means of automating the release version of a git repo using git tags',
                 author='Michael Schappacher',
                 author_email='m.a.schappacher@gmail.com',
                 install_requires=install_requires,
                 packages=["cloudmitigator_semantic"],
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 entry_points="""
                    [console_scripts]
                    semantic=cloudmitigator_semantic.cli:semantic
                 """
                 )