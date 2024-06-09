class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("Available flavors: " + ", ".join(self.flavors))

ice_cream_stand = IceCreamStand("Sweet Treats")
ice_cream_stand.flavors = ["vanilla", "chocolate", "strawberry"]
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
