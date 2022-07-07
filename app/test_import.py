"""Primary logic for the ``test-import`` application"""

from argparse import ArgumentParser
import sys

class TestImport(ArgumentParser):
    """A demo command line application that verifies package requirements are installed"""

    @classmethod
    def execute(cls):
        """Execute the application"""

        print(f'Using Pytjon {sys.version} - {sys.path}')

        import pandas
        print('Pandas was imported successfully!')
        import datasets
        print('Datasets was imported successfully!')
        import cellrank
        print('Cellrank was imported successfully!')
