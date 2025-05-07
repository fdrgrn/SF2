class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = odometer_reading

    def __repr__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Odomoter reading: {self.odometer_reading}"
    
    def odometerChange(self, new_reading : int) -> None:
        if self.odometer_reading > new_reading:
            print("Cannot lower Odometer reading")
        else:
            self.odometer_reading = new_reading

    def readOdometer(self) -> None:
        print(f"This car has {self.odometer_reading} miles left")


    