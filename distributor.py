import sys

from src.compilers import Clang, GCC
from src.utils import unsupported
from src.Task import Task
from src import Actions


COMPILERS = (Clang, GCC)


def run(command: list[str]):
    compiler_objs = [compiler(command) for compiler in COMPILERS]
    is_compiler = [compiler_obj.is_valid() for compiler_obj in compiler_objs]

    if sum(is_compiler) == 1:
        compiler_obj = compiler_objs[is_compiler.index(True)]

        print(f'Executing {compiler_obj.name} on {compiler_obj.arguments.source_files}')
        Task(compiler_obj).execute()

    else:
        if any(is_compiler):
            unsupported(f'Multiple compilers found for command "{command}". Defaulting to regular execution')

        print(f'Executing regular command "{command}"')
        Task(Actions.RunProcess(command)).execute()


if __name__ == '__main__':
    run(sys.argv[1:])
