"""Installation instructions for the tell-me-about application"""

import re
from pathlib import Path

from setuptools import setup, find_packages


def get_long_description():
    """Return a long description of tha parent package"""

    readme_file = Path(__file__).parent / 'README.md'
    return readme_file.read_text()


def get_requirements():
    """Return a list of package dependencies"""

    requirements_path = Path(__file__).parent / 'requirements.txt'
    with requirements_path.open() as req_file:
        return req_file.read().splitlines()


def get_meta():
    """Return package metadata including the:
        - author
        - version
        - license
    """

    init_path = Path(__file__).resolve().parent / 'app/__init__.py'
    init_text = init_path.read_text()

    version_regex = re.compile("__version__ = '(.*?)'")
    version = version_regex.findall(init_text)[0]

    author_regex = re.compile("__author__ = '(.*?)'")
    author = author_regex.findall(init_text)[0]

    license_regex = re.compile("__license__ = '(.*?)'")
    license_type = license_regex.findall(init_text)[0]

    return author, version, license_type


_author, _version, _license_type = get_meta()
setup(
    name='tell-me-about',
    description='An example command line application written in Python',
    version=_version,
    packages=find_packages(),
    python_requires='>=3.9',
    entry_points="""
        [console_scripts]
        tell-me=app.app_logic:App.execute
    """,
    install_requires=get_requirements(),
    author=_author,
    keyword='example, command-line, app',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    license=_license_type,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)
