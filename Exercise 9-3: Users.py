class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

user1 = User("John", "Doe", 28, "New York")
user2 = User("Jane", "Smith", 34, "Los Angeles")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
