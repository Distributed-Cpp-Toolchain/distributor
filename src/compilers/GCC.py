import sys
import re

if __name__ == '__main__':
    sys.path.append('../')

from src.Actions import Action, RunProcess
from src.utils import unsupported


GCC_VERSION_REGEX = r'g(?:cc|\+\+).+?(\d+\.\d+\.\d+)'


class GCC(Action):
    def __init__(self, arguments: list[str]):
        self.executable = arguments[0]
        self.arguments = arguments[1:]

        print(self.get_version())

    def get_version(self) -> str:
        output, error = RunProcess([self.executable, '--version']).execute()
        match = re.fullmatch(GCC_VERSION_REGEX, output.splitlines()[0], re.IGNORECASE)
        assert not error and match, unsupported(f'gcc --version:\n{output}\n{error}')
        return match.group(1)

    def get_dependencies(self):
        pass

    def execute(self):
        return RunProcess([self.executable, *self.arguments]).execute()
