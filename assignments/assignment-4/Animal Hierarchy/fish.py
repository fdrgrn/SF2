from animal import Animal

class Fish(Animal):
    # def __init__(self, legs=0, fins=2, wings=0):
    #     super().__init__(legs, fins, wings)

    # def move(self) -> None:
    #     print("Fish move with their fins.")

    # def sleep(self) -> None:
    #     print("Fish rest and reduce their energy.")

    def reproduce(self) -> None:
        print("Fish reproduction varies largely, some give birth to live young while others lay eggs.")

    def __repr__(self) -> str:
        return f'{super().__repr__()}\nClass: Fish'