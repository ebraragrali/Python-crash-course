class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("John", "Doe", 28, "New York")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
