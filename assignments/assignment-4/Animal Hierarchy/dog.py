from mammal import Mammal
from pet import Pet
from omnivore import Omnivore

class Dog(Mammal, Omnivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        self.ears = ears 

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}\n"
            f"{Pet.__repr__(self)}\n"
            f"Species: Dog\n\n"
            f"{Omnivore.__repr__(self)}\n"
        )

    def move(self):
        print("Dogs move around with their 4 legs")

    def sleep(self):
        print("Dogs are usually up during the day but take regular naps")

    def eat(self):
        Omnivore.eat(self)
        print("Dogs eat anything from kibble to leftovers!")
    
    def reproduce(self):
        super().reproduce(self)
        print("Dogs give litters")

    def pet(self):
        Pet.pet(self)
        print("Dogs are one of the top most popular pets in the world")