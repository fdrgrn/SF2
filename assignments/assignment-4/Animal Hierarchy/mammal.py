from animal import Animal

class Mammal(Animal):
    def reproduce(self) -> None:
        print("Mammals give birth to live young, and raise them until they can be independent.")

    def __repr__(self) -> str:
        return f'{super().__repr__()}\nClass: Mammal'