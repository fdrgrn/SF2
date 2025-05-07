# from abc import ABCMeta

from mammal import Mammal
from pet import Pet
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        # Mammal.__init__(self, legs)
        self.ears = ears 

            
    def reproduce(self) -> None:
        super().reproduce(self)
        print("Bunnies make litters")

    def move(self):
        print("Bunnies move aroubd by hopping")

    def sleep(self):
        print("Bunnies are nocyturnal and sleep around 12 hours per day")

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}\n"
            f"{Herbivore.__repr__(self)}\n"
            f"{Pet.__repr__(self)}\n"
            f"Species: Bunny"
        )

    def pet(self):
        Pet.pet(self)
        print("Bunnies are small animals that love to be pet")

    def eat(self):
        Herbivore.eat(self)
        print("Bunnies mostly eat grass and fruit pellets")

if __name__ == '__main__':
    b1 = Bunny()
    print(b1)

    b1.sleep()
    b1.move()




    