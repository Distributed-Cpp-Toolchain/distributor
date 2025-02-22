from src.utils import mkpath
from src.Task import Task
from src import Actions


TESTS_DIR = 'tests/'


def run_nocc_sample():
    Task(Actions.RunProcess(
        'g++ 1.cpp -o 1.o -c',
        mkpath(TESTS_DIR, 'nocc_sample')
    )).execute()


def run_tests():
    run_nocc_sample()


if __name__ == '__main__':
    run_tests()
