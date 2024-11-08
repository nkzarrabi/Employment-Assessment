class CoreValues:
    def __init__(self):
        self.values: Dict[str,float] = {}

    def add_value(self, name, weight):
        self.values[name] = weight

    def remove_value(self, name):
        if name in self.values:
            del self.values[name]
        else:
            raise KeyError(f"The value '{name}' is not in the list of values")

        if name in self.values:
            self.values[name] = weight
        else:
            raise KeyError(f"The value '{name}' is not in the list of values")

    def adjust_weighting(self, name, weight):
        if name in self.values:
            self.values[name] = weight
