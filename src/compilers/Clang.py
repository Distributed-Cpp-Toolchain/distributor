import sys
import re

if __name__ == '__main__':
    sys.path.append('../')

from src.Actions import Action, RunProcess
from src.utils import unsupported


CLANG_VERSION_REGEX = r'.*clang(?:\+\+)?\s*version\s*(\d+\.\d+\.\d+).*'


class Clang(Action):
    name = 'Clang'

    def __init__(self, command: list[str]):
        self.executable = command[0]
        self.arguments = command[1:]

    def is_valid(self):
        try:
            self.get_version()
            return True
        except AssertionError:
            return False

    def get_version(self) -> str:
        output, error = RunProcess([self.executable, '--version']).execute()
        match = re.fullmatch(CLANG_VERSION_REGEX, output.splitlines()[0], re.IGNORECASE)
        assert not error and match, unsupported(f'clang --version:\n{output}\n{error}')
        return match.group(1)

    def get_dependencies(self):
        pass

    def execute(self):
        return RunProcess([self.executable, *self.arguments]).execute()
