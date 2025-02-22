import subprocess
import os


def run(directory: str, command: str):
    os.chdir(directory)
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = map(lambda x: x.decode('utf-8').strip(), process.communicate())
    return output, error


def run_nocc_test():
    path = 'test/nocc_test/'
    command = 'g++ 1.cpp -o 1.o -c'
    run(path, command)


def clean_nocc_test():
    for file in os.listdir('test/nocc_test/'):
        if os.path.splitext(file)[1] == '.o':
            os.remove(f'test/nocc_test/{file}')


def run_tests():
    run_nocc_test()


# def clean_tests():
#     clean_nocc_test()


if __name__ == "__main__":
    # clean_tests()
    run_tests()
