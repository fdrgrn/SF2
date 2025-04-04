print("Enter two numbers that I will divide for you")
print("Enter \'q'\'to quit at anytime")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Cannot divide given number by 0")
    except ValueError:
        print("Please enter intergers")
    else:
        print(f"Result is: {result}")
print("Succesful quit")