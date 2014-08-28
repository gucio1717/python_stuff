from mfw.controller import Controller


class RpSoftware(Controller):

    def __init__(self, file):
        super().__init__()
        self._file = file

    def generate(self):
        return [1, 2, 3]
