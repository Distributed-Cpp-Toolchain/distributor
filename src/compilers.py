from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Iterator
import sys
import re

if __name__ == '__main__':
    sys.path.append('../')

from src.Actions import Action, RunProcess
from src.utils import unsupported


class Compiler(Action, ABC):
    name: str
    version_regex: str

    def __init__(self, command: list[str]):
        self.executable = command[0]
        self.arguments = CompilerArguments(command[1:])

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


@dataclass
class CompilerArguments:
    arguments: list[str]
    source_files: list[str] = field(default_factory=list)
    output_files: list[str] = field(default_factory=list)
    include_dirs: list[str] = field(default_factory=list)
    defines: list[str] = field(default_factory=list)
    options: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)

    def __post_init__(self):
        self._parse_arguments()

    def _parse_arguments(self):
        it = iter(self.arguments)

        for arg in it:
            if arg.endswith(('.cpp', '.c', '.cc', '.cxx', '.h', '.hpp')):
                self.source_files.append(arg)

            elif arg in ('-o', '--output'):
                self.output_files.append(next(it, ''))

            elif arg.startswith('-I'):
                self.include_dirs.append(arg[2:] if len(arg) > 2 else next(it, ''))

            elif arg.startswith('-D'):
                self.defines.append(arg[2:] if len(arg) > 2 else next(it, ''))

            elif arg in ('-c', '-Wall', '-Wextra', '-Werror', '-fPIC') or arg.startswith('-std='):
                self.flags.append(arg)

            elif arg.startswith('-M') or arg in ('-MD', '-MT', '-MF'):
                self.options.append(arg)
                if arg in ('-MT', '-MF'):
                    self.options.append(next(it, ''))

            elif arg.startswith('-Xclang'):
                self.options.append(arg)
                self.options.append(next(it, ''))

            else:
                unsupported(f'Unsupported compiler argument: {arg}')

    def __iter__(self) -> Iterator[str]:
        return iter(self.arguments)


# ----------------------------------------------------------------------------------------------------------------------

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
