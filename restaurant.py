# Restaurant Management Program
# This program defines a Restaurant class with attributes such as the restaurant's name and cuisine type.
# It also provides methods to describe the restaurant and indicate when it is open.
# Finally, it demonstrates how to create multiple restaurant objects and display their information.

class Restaurant:
    def __init__(self, name, cousine_type):
        self.name = name  # Store the name of the restaurant
        self.cousine_type = cousine_type  # Store the type of cuisine
        self.number_served = 0
        self.now_served = 0

    # def describe_restaurant(self):
    #     print(f"{self.name}, {self.cousine_type}")  # Output the name and cuisine

    @property
    def open_restaurant(self):
        return f"{self.name} is open"  # Return a string indicating the restaurant is open
    
    def set_number_served(self):
        self.number_served = int(input(f"{self.name}'s number served: "))

    def increment_number_served(self):
        self.now_served = int(input(f"{self.name}'s now served: "))
        self.number_served += self.now_served  # Update total number served by adding now served to number served


    def __str__(self):
        return f"{self.name}, {self.cousine_type}"  # Return name and cuisine in string form

# Create a list of restaurant objects
restaurants = [
    Restaurant("Moreno's", "Mexican"),   # Mexican restaurant
    Restaurant("The Gym", "American"),   # American restaurant
    Restaurant("Olive Garden", "Italian")  # Italian restaurant
]

def main():
# Loop through the list of restaurants and print information about each
    for restaurant in restaurants:
        restaurant.set_number_served()  # Set initial number served
        before_increment = restaurant.number_served  # Save the number served before increment
        restaurant.increment_number_served()  # Increment the number served
        # Print a message that the restaurant is open, along with its cuisine type
        print(f"{restaurant.open_restaurant} for {restaurant.cousine_type} food and early it served {before_increment} people")
        print(f"{restaurant.open_restaurant} has NOW served {restaurant.number_served} people")

if __name__=="__main__":
    main()