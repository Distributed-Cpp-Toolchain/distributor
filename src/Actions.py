from abc import ABC, abstractmethod
from dataclasses import dataclass
import shutil

import subprocess
import os


@dataclass
class Action(ABC):
    @abstractmethod
    def execute(self):
        pass


# -------------------------------------------------- File operations ---------------------------------------------------

@dataclass
class WriteFile(Action):
    path: str
    content: str
    mode: str = 'w'

    def execute(self):
        with open(self.path, self.mode) as file:
            file.write(self.content)


@dataclass
class CopyFile(Action):
    src: str
    dst: str

    def execute(self):
        shutil.copy2(self.src, self.dst)


@dataclass
class MoveFile(Action):
    src: str
    dst: str

    def execute(self):
        shutil.move(self.src, self.dst)


@dataclass
class DeleteFile(Action):
    path: str

    def execute(self):
        os.remove(self.path)


# ------------------------------------------------- Folder operations --------------------------------------------------

@dataclass
class MakeDirectory(Action):
    path: str

    def execute(self):
        os.makedirs(self.path)


@dataclass
class CopyDirectory(Action):
    src: str
    dst: str

    def execute(self):
        shutil.copytree(self.src, self.dst)


@dataclass
class MoveDirectory(Action):
    src: str
    dst: str

    def execute(self):
        shutil.move(self.src, self.dst)


@dataclass
class RemoveDirectory(Action):
    path: str

    def execute(self):
        shutil.rmtree(self.path)


# --------------------------------------------- General process operations ---------------------------------------------

@dataclass
class RunProcess(Action):
    command: str | list[str]
    working_directory: str = '.'

    def execute(self):
        process = subprocess.Popen(
            self.command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.working_directory
        )
        output, error = (item.decode('utf-8').strip() for item in process.communicate())
        return output, error
