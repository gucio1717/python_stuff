from mfw.controller import Controller


class Alloc(Controller):

    def __init__(self, features):
        super().__init__()
        self.features = features

    def generate(self):
        self.logger.info('Generating Alloc')
        # Prepare data... use model class to load it?
        data = {'rps': ['1', '2', '80']}

        self.load_view('demo', data)
        self.load_view('features/' + self.features[0]+'/demo', data)
        return self.result
