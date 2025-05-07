from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def eat(self) -> None:
        print("I eat meat.")

    def __repr__(self) -> str:
        return "This organism is a carnivore. It feeds on other animals, and its physical features facilitate hunting."