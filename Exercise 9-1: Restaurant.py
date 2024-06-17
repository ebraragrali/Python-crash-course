class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

restaurant = Restaurant("La Piazza", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
