file_name = 'book_txt'
try:
    input_file = open(file_name, 'r')
except FileNotFoundError:
    print("File does not exist in this directory")
    output_file = open(file_name, 'w', encoding="UTF8")
else:
    for line in input_file:
        print(line.rstrip())

input_file = open('story_file.txt', 'r')
temp_list = input_file.readlines()
output_file.writelines(temp_list)

count = 0
for line in temp_list:
    print(line)
    count += len(line.split())
print(count)


input_file.close()
output_file.close()