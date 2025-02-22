from src.Actions import Action, RunProcess


class GCC(Action):
    def __init__(self, arguments: list[str]):
        self.executable = arguments[0]
        self.arguments = arguments[1:]

    def get_dependencies(self):
        pass

    def execute(self):
        return RunProcess([self.executable, *self.arguments]).execute()
