"""
This is from the book Python Crash Course, page 162
"""
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type



    def describe_restaurant(self):
        print(f"Restaurant Name is {self.name}")
        print(f"Cuisine Type of the Restaurant is {self.cuisine_type}")
              
    def open_restaurant(self):
        print(f"The restaurant {self.name} is open!")


restaurant1  = Restaurant("Valentino's", 'Italian')
restaurant2 = Restaurant("Mario's", 'American')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @property
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

        
my_new_car = Car('audi', 'a4', '2024')

print(my_new_car.get_descriptive_name)

