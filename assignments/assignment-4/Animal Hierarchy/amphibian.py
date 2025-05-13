from animal import Animal

class Amphibian(Animal):
    # def __init__(self, legs=4, fins=0, wings=0):
    #     super().__init__(legs, fins, wings)

    # def move(self) -> None:
    #     print("Amphibians' movements depend on the species.")

    # def sleep(self) -> None: 
    #     print("Amphibians sleep to save their energy.")

    def reproduce(self) -> None:
        print("Amphibians reproduce by laying soft eggs in the water.")

    def __repr__(self) -> str:
        return f'{super().__repr__()}\nClass: Amphibian'