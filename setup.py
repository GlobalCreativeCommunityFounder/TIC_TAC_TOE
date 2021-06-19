from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='TIC_TAC_TOE',
    version='1',
    packages=['TIC_TAC_TOE'],
    url='https://github.com/GlobalCreativeCommunityFounder/TIC_TAC_TOE',
    license='MIT',
    author='GlobalCreativeCommunityFounder',
    author_email='globalcreativecommunityfounder@gmail.com',
    description='This package contains implementation of the game "TIC_TAC_TOE" on command line interface'
                ' where the player plays as crosses X\'s and the opponent plays as circles O\'s).',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "TIC_TAC_TOE=TIC_TAC_TOE.tic_tac_toe:main",
        ]
    }
)