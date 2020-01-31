import setuptools

requirements_files = ['requirements.txt']

install_requires = []

for requirements_file in requirements_files:
    with open(requirements_file, 'r') as f:
        install_requires += f.readlines()

setuptools.setup(name='cloudmitigator_semantic',
                 version='0.0.1',
                 description='Means of automating the release version of a git repo using git tags',
                 author='Michael Schappacher',
                 author_email='m.a.schappacher@gmail.com',
                 install_requires=install_requires,
                 packages=["cloudmitigator_semantic"],
                 entry_points="""
                    [console_scripts]
                    semantic=cloudmitigator_semantic.__main__:determine_if_bump_has_occurred
                 """
                 )
