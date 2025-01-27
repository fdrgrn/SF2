number = int(input("Enter number: "))
number = number + 1

def verify_number(number):
    digits = str(number)
    if len(digits) == len(set(digits)):
        return True

while True:
    found = verify_number(number)
    if not found:
        number += 1
    else:
        print(number)
        break
