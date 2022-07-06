"""Installation instructions for the tell-me-about application"""

from pathlib import Path

from setuptools import setup, find_packages


def get_long_description():
    """Return a long description of tha parent package"""

    readme_file = Path(__file__).parent / 'README.md'
    return readme_file.read_text()


def get_requirements():
    """Return a list of package dependencies"""

    requirements_file = Path(__file__).parent / 'requirements.txt'
    return requirements_file.read_text().split()


setup(
    name='tell-me-about',
    description='An example command line application written in Python',
    version='0.0.1',
    packages=find_packages(),
    python_requires='>=3.9',
    entry_points="""
        [console_scripts]
        tell-me=app.app_logic:App.execute
    """,
    install_requires=get_requirements(),
    author='Pitt Center for Research Computing',
    keyword='example, command-line, app',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/CITGuru/cver',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)
