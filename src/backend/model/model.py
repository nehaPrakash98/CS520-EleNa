"""
Model class to encapsulate all data
- Source : Starting point
- Destination : End point
- Limit : Amount of deviation allowed
- Mode : Maximize/ Minimize
- Algorithm : Algorithm to use for finding navigation route
"""


class Model(object):

    def _init_(self):
        self.source = None
        self.destination = None
        self.limit = None
        self.mode = None
        self.algorithm = None

    # setters
    def set_source(self, s):
        self.source = s

    def set_destination(self, d):
        self.destination = d

    def set_mode(self, mode):
        self.mode = mode

    def set_limit(self, o):
        self.limit = o

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    # Getters
    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_mode(self):
        return self.mode

    def get_limit(self):
        return self.limit

    def get_algorithm(self):
        return self.algorithm
