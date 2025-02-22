import sys

from src.Task import Task
from src.compilers.GCC import GCC
from src import Actions


def run(arguments):
    if arguments[0].lower() in ('gcc', 'g++'):
        gcc = GCC(arguments)
        print(f'Executing GCC command "{gcc.executable} {" ".join(gcc.arguments)}"')
        Task(gcc).execute()

    else:
        print(f'Executing regular command "{' '.join(arguments)}"')
        Task(Actions.RunProcess(
            arguments
        )).execute()


if __name__ == '__main__':
    run(sys.argv[1:])
