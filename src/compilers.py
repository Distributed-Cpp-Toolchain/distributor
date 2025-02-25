import sys
import re
from abc import ABC, abstractmethod

if __name__ == '__main__':
    sys.path.append('../')

from src.Actions import Action, RunProcess
from src.utils import unsupported


class Compiler(Action, ABC):
    name: str
    version_regex: str

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
        match = re.fullmatch(self.version_regex, output.splitlines()[0], re.IGNORECASE)
        assert not error and match, unsupported(f'{self.executable} --version:\n{output}\n{error}')
        return match.group(1)

    @abstractmethod
    def get_dependencies(self):
        pass

    def execute(self):
        return RunProcess([self.executable, *self.arguments]).execute()


class Clang(Compiler):
    name = 'Clang'
    version_regex = r'.*clang(?:\+\+)?\s*version\s*(\d+\.\d+\.\d+).*'

    def __init__(self, command: list[str]):
        super().__init__(command)

    def get_dependencies(self):
        # TODO
        pass


class GCC(Compiler):
    name = 'GCC'
    version_regex = r'g(?:cc|\+\+).+?(\d+\.\d+\.\d+)'

    def __init__(self, command: list[str]):
        super().__init__(command)

    def get_dependencies(self):
        # TODO
        pass
