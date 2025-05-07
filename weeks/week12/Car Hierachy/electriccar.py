from car import Car
from battery import Battery

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def fillGastank(self) -> None:
        print("This car does not take gas")

if __name__ == "__main__":
    electric_car = ElectricCar("BYD", "Car", 2025)
    print(electric_car)
    



        