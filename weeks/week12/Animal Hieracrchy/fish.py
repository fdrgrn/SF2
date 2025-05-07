from __future__ import annotations
from animal import Animal
class Fish(Animal):
    def __init__(self, colour):
        super().__init__(0)
        self.type = 'fish'
        self.colour = colour.lower()

    def walk(self) -> None:
        print("Fish cannot walk")

    def sleep(self) -> None:
        print('Fish reduce their activity and metabolism to swin')

    def __repr__(self):
        return f"Animal: {self.type} \nColour: {self.colour}"
    
    def changeColour(self, new_colour: str) -> None:
        self.colour = new_colour
    
    def sameColour(self, other: Fish) -> bool:
        return isinstance(other, Fish) and self.colour == other.colour
    
if __name__ == "__main__":
    fish = Fish("Blue")
    print(fish)

    fish.sleep()
    fish.walk()

    fish.changeColour("Pink black stripes")
    print(fish)

    fish2 = Fish("Blue")
    print(fish.sameColour(fish2))