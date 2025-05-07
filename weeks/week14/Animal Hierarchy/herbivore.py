from heterotroph import Heterotroph

class Herbivore(Heterotroph):
    def eat(self) -> None:
        print("I eat plants.")

    def __repr__(self) -> str:
        return "This organism is a herbivore. It feeds on plant matter and its physiology facilitates food search."
