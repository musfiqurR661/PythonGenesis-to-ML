#OOP: Class define, object creation

# Define a class named "Car"
class Car:
    # Constructor method to initialize the car object with its attributes
    def __init__(self, make, model, year):
        self.make = make  # Attribute: make of the car
        self.model = model  # Attribute: model of the car
        self.year = year  # Attribute: manufacturing year of the car

    # Method to display information about the car
    def display_info(self):
        print(f"Car: {self.make} {self.model} {self.year}")

# Create an object of the Car class
car1 = Car("Toyota", "Camry", 2020)

# Call the display_info method to display information about the car
car1.display_info()
