import os


def mkpath(*paths: str) -> str:
    return os.path.normpath(os.path.join(*paths))


def unsupported(message: str) -> str:
    return f'Encountered unsupported feature, please report all the details to the developers:\n{message}'
