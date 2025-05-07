from heterotroph import Heterotroph

class Omnivore(Heterotroph):
    def eat(self) -> None:
        print("I eat anything!")

    def __repr__(self) -> str:
        return "This organism is an omnivore. It can feed on both plants and other animals."
