from src.utils import mkpath
from src.Task import Task
from src import Actions


TESTS_DIR = 'tests/'


def run_nocc_sample():
    Task(Actions.RunProcess(
        'g++ 1.cpp -o 1.o -c',
        mkpath(TESTS_DIR, 'nocc_sample')
    )).execute()


# def clean_nocc_sample():
#     for file in os.listdir(mkpath(TESTS_DIR, 'nocc_sample')):
#         if os.path.splitext(file)[1] == '.o':
#             os.remove(mkpath(TESTS_DIR, 'nocc_sample', file))


def run_tests():
    run_nocc_sample()


# def clean_tests():
#     clean_nocc_sample()


if __name__ == '__main__':
    # clean_tests()
    run_tests()
