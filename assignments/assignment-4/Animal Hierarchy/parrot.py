from bird import Bird
from pet import Pet
from omnivore import Omnivore

class Parrot(Bird, Omnivore, Pet):
    def __init__(self, legs = 2, colour = 'yellow', wings = 2):
        super().__init__(legs)
        self.colour = colour 
        self.wings = wings

            
    def reproduce(self) -> None:
        super().reproduce(self)
        print("Parrots often take a few days to lay a full clutch of eggs. This can be as many\
              as three to four eggs")

    def move(self):
        print("I can move in various ways. I can fly, walk, climb and even use a unique method called 'beakiation' to traverse narrow branches.")

    def sleep(self):
        print("Parrots sleep from 10 to 12 hours per night, often tucked between their wings. They also often takes naps at night.")

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}\n"
            f"{Pet.__repr__(self)}\n"
            f"Species: Parrot\n\n"
            f"{Omnivore.__repr__(self)}"
        )

    def pet(self):
        Pet.pet(self)

    def eat(self):
        Omnivore.eat(self)
        print("I eat both plant and animal matter. My natural diet involves various foods like nuts, seed, flowers, buds and insects.")

if __name__ == "__main__":
    p1 = Parrot()
    print(p1)
    p1.eat()
    p1.move()
    p1.sleep()
    p1.pet()