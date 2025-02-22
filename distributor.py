import sys

from src.Task import Task
from src import Actions


def run(arguments):
    print(f'Running "{arguments}"')
    Task(Actions.RunProcess(
        arguments
    )).execute()


if __name__ == '__main__':
    run(sys.argv[1:])
