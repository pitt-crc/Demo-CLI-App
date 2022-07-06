"""Primary logic for the ``tell-me`` application"""

from argparse import ArgumentParser


class TellMe(ArgumentParser):
    """A demo command line application that echos back given text"""

    def __init__(self):
        """Define command line arguments and help text"""

        super().__init__()
        self.add_argument('text', type=str, nargs='?', help='text to echo back')

    @classmethod
    def execute(cls):
        """Execute the application"""

        app = cls()
        args = app.parse_args()
        print(f'I will tell you about: {" ".join(args.text)}')
