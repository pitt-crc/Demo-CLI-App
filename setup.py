"""Installation instructions for the tell-me-about application"""

from pathlib import Path

from setuptools import setup, find_packages

README_FILE = Path(__file__).parent / "README.md"
README_TEXT = README_FILE.read_text()

setup(
    name='tell-me-about',
    description='An example command line application written in Python',
    version='0.0.1',
    packages=find_packages(),
    python_requires='>=3.9',
    author='Pitt Center for Research Computing',
    keyword='example, command-line, app',
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/CITGuru/cver',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)
