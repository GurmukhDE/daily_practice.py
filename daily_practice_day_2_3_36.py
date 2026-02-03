# Let's understand the class in oops


class Car:
    def __init__(self, brand,model, country):
        self.brand = brand
        self.model = model
        self.country = country

car_info = Car("Ford", "Bronco", "USA")
print(car_info.brand,car_info.model, car_info.country)


class CarInventory:
    def __init__(self, cars):
        self.cars = cars   # list of dicts

    def print_all_cars(self):
        for car in self.cars:
            print(car["brand"], car["model"], car["country"])


cars_data = [
    {"brand": "Ford", "model": "Bronco", "country": "USA"},
    {"brand": "BMW", "model": "X5", "country": "Germany"},
    {"brand": "Tata", "model": "Safari", "country": "India"}
]

inventory = CarInventory(cars_data)
inventory.print_all_cars()








