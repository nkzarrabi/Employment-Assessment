from core_values import CoreValues

class HRInterface:
    def __init__(self):
        self.core_values = CoreValues()

    def display_core_values(self):
        for name, weight in self.core_values.values.items():
            print(f"Core Value: {name}, Weight: {weight}")

    def add_core_value(self, name, weight):
        self.core_values.add_value(name, weight)
        print(f"Added core value: {name} with weight: {weight}")

    def remove_core_value(self, name):
        self.core_values.remove_value(name)
        print(f"Removed core value: {name}")

    def update_core_value(self, name, weight):
        self.core_values.update_value(name, weight)
        print(f"Updated core value: {name} to weight: {weight}")

    def adjust_core_value_weighting(self, name, weight):
        self.core_values.adjust_weighting(name, weight)
        print(f"Adjusted core value: {name} to new weight: {weight}")

# Example usage
if __name__ == "__main__":
    hr_interface = HRInterface()
    hr_interface.add_core_value("Collaboration", 0.3)
    hr_interface.add_core_value("Innovation", 0.4)
    hr_interface.add_core_value("Adaptability", 0.3)
    hr_interface.display_core_values()
    hr_interface.adjust_core_value_weighting("Collaboration", 0.35)
    hr_interface.display_core_values()
