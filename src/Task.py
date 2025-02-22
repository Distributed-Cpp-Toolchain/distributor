import sys

if __name__ == '__main__':
    sys.path.append('../')

from src.Actions import Action


class Task:
    def __init__(self, *actions: Action):
        self.actions = actions

    def execute(self):
        for action in self.actions:
            action.execute()


if __name__ == '__main__':
    task = Task([])
