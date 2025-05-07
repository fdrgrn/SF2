from animal import Animal

#ASK ABOUT WRAPPERS FOR THE TEST
class Cat(Animal):
    def __init__(self):
       super().__init__(4)
       #Animal.__init__(self, 4)
       self.type = 'cat'

    def sleep(self, hours = None) -> None:
        if hours == None:
           print("Cats sleep in warm and comfortable places")
        else:
            print(f"Cats sleep for {hours} hours per day")

    def __repr__(self) -> str:
        return f"Animal: {self.type} \nLegs: {self.legs}"

if __name__ == "__main__":
    cat = Cat()
    print(cat)

    print(cat.walk())
    print(cat.sleep())
    print(cat.sleep(12))
            