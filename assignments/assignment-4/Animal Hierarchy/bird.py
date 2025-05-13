from animal import Animal

class Bird(Animal):
    def reproduce(self) -> None:
        print("Members of this kingdom reproduce by finding a mate of the same sepcies. Birds \
              typically reproduce by hatchhing and incubating their eggs.")

    def __repr__(self) -> str:
        return f'{super().__repr__()}\nClass: Bird'