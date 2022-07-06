"""Primary logic for the ``test-import`` application"""

from argparse import ArgumentParser


class TestImport(ArgumentParser):
    """A demo command line application that verifies package requirements are installed"""

    @classmethod
    def execute(cls):
        """Execute the application"""


        import pandas
        print('Pandas imported')
        import datasets
        print('Datasets imported')
        import matplotlib
        print('Matplotlib imported')
