from animal import Animal

class Reptile(Animal):
    # def __init__(self, legs=4, fins=0, wings=0):
    #     super().__init__(legs, fins, wings)

    # def move(self) -> None:
    #     print("Reptiles move using their limbs.")

    # def sleep(self) -> None:
    #     print("Reptiles sleep to conserve energy.")

    def reproduce(self) -> None:
        print("Reptiles reproduce by laying eggs, typically on land rather than water.")

    def __repr__(self) -> str:
        return f'{super().__repr__()}\nClass: Reptile'