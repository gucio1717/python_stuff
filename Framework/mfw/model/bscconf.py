'''
Created on 8 kwi 2014

@author: eszcmic
'''
from mfw.model import Model


class BscConf(Model):

    def __init__(self, file):
        self.data = []
        if file:
            self.load_data(file)

    def load_data(self, file):
        with open(file, 'r') as f:
            self.data = f.readlines()
            self.data = list(map((lambda x: x.strip()), self.data))

    def __iter__(self):
        return iter(self.data)
