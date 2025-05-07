class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describeBattery(self):
        print(f"this car has a battery of {self.battety_size} -kWh")

    def batteryChange(self, new_battery: int) -> None:
        self.battery_size = new_battery

    def getRange(self) -> None:
        if self.battery_size == 40:
            print("Mileage of 150")
        elif self.battery_size == 60:
            print("Mileage is 225")