def clean(address):
    address = address.lower()
    clean_address = ""
    for char in address:
        if 33 <= ord(char) <= 37 or not 58 <= ord(char) <= 63:
            pass
        else:
            clean_address = clean_address + char
    print(clean_address)

clean("hello.+_hibye@gmail")
#number of email adddresses
n = int(input("Number of email addresses:"))
for i in range(n):
    email_address = input(f"Email address {i+1}: ")

clean("hello.+_hibye@gmail")