class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is now open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant("La Piazza", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(150)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Number served: {restaurant.number_served}")
