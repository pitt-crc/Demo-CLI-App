"""Primary logic for the ``test-import`` application"""

from argparse import ArgumentParser


class TestImport(ArgumentParser):
    """A demo command line application that verifies package requirements are installed"""

    @classmethod
    def execute(cls):
        """Execute the application"""


        import pandas
        print('Pandas was imported successfully!')
        import datasets
        print('Datasets was imported successfully!')
        import matplotlib
        print('Matplotlib was imported successfully!')
