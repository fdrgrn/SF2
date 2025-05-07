from animal import Animal

class Mammal(Animal):
    def __init__(self, legs=4, fins=0, wings=0):
        super().__init__(legs, fins, wings)

    def move(self) -> None:
        print("Mammals move using their legs.")

    def sleep(self) -> None:
        print("Mammals sleep schedules depend on the species")

    def reproduce(self) -> None:
        print("Mammals give birth to live young, and raise them until they can be independent.")

    def __repr__(self) -> str:
        return f'Kingdom: Animalia\nClass: Mammal'