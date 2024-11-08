class CoreValues:
    def __init__(self):
        self.values: Dict[str,float] = {}

    def add_value(self, name, weight):
        self.values[name] = weight

    def remove_value(self, name):
        if name in self.values:
            del self.values[name]

    def update_value(self, name, weight):
        if name in self.values:
            self.values[name] = weight

    def adjust_weighting(self, name, weight):
        if name in self.values:
            self.values[name] = weight
