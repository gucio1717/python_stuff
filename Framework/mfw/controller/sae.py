from mfw.controller import Controller


class Sae(Controller):

    def __init__(self, features):
        super().__init__()
        self.features = features

    def generate(self):
        self.logger.info('Generating SAE')
        return '#This is SAE\nSAECMD:VALUE=125;\n'
