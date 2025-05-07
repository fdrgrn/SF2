class Animal:
    def __init__(self, legs = 0):
        self.legs = legs

    def walk(self) -> None:
        print(f"This animal walks with {self.legs} legs")

    def sleep(self) -> None:
        print("Different animals have different sleeping habits")

    def __repr__(self):
        return f"Animal: No Idea \nLegs: {self.legs}"

if __name__ == '__main__':
    anim = Animal(6)
    print(anim)
    anim.walk()
    anim.sleep()
