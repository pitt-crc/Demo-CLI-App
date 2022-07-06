"""Primary logic for the command line application"""

from argparse import ArgumentParser


class App(ArgumentParser):
    """A demo command line application that echos given text."""

    def __init__(self):
        """Define command line arguments and help text"""

        super().__init__()
        self.add_argument('text', type=str, help='text to echo back')

    @classmethod
    def execute(cls):
        """Execute the application"""

        app = cls()
        args = app.parse_args()
        print(f'You told me: {args.text}')
