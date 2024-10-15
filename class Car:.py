class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year}, {self.make}, {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"{self.make}, {self.model} has {self.odometer_reading} miles.")

    def update_odometer(self):
        mileage = int(input(f"{self.make}, {self.model} Initial miles: "))
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the Odometer.")
            return False
        return True
    
    def increment_odometer(self):
        miles = int(input(f"Added miles to {self.make}, {self.model}: "))
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=0):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        self.battery_size = int(input("Enter battery size (40 / 65)kWh: "))
        if self.battery_size in [40, 65]:
            print(f"{self.get_descriptive_name()} has a {self.battery_size}-kWh battery.")
        else:
            print("Invalid input for battery size.")


def main():
    cars = [
        Car("Ford", "F150", 2011), 
        Car("Toyota", "Corolla", 2019),
        Car("Ford", "Ranger", 2003),
        Car("Nissan", "Versa", 2020),
        ElectricCar("Tesla", "Model Y", 2023)  # ElectricCar
    ]

    for car in cars:
        if car.update_odometer():
            print(car.get_descriptive_name())
            car.increment_odometer()
            car.read_odometer()
            # Check if the car is an ElectricCar before calling describe_battery
            if isinstance(car, ElectricCar):  # This checks if the car is an instance of ElectricCar
                car.describe_battery()


if __name__ == "__main__":
    main()
