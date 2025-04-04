# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''
read_file = open('story_file.txt', 'r')
word_count = 0
word_frequency = {}
for line in read_file:
    print(line)
    word_count += len(line.split())
    for word in line.split():
        word = word.lower().strip('"')
        word_frequency[word] = word_frequency.get(word, 0) + 1
read_file.close()

new_d = {}
#Inverse value and keys
for word in word_frequency:
    if word_frequency[word] in new_d:
        new_d[word_frequency[word]].append(word)
    else:
        new_d[word_frequency[word]] = [word]

print(f"\nWord count: {word_count}\n")
for key in sorted(new_d.keys()):
    print(f"{new_d[key]}: {key}")
    
# Question 2
'''
Make two files: cats.txt and dogs.txt.  Store at least three names of cats in the first
file and three names of dogs in the second file.  Write a program that tries to read
these files and print the contents of each file to the screen.  

(a) Wrap your code in a try-except block to catch the FileNotFoundError and print a 
    friendly message if a file is missing.  To test your code, move one of the files 
    to a different location on your system, and make sure that the code in the except 
    block executes properly.  
(b) Modify your previous code to fail silently if either file is missing
'''
try:
    cat_file = open('cats.txt', 'r')
except FileNotFoundError:
    pass
    #b) print("'cats.txt' was not found")
else:
    print(cat_file.read())

try:
    dog_file = open('dogs.txt', 'r')
except FileNotFoundError:
    pass
    #b) print("'dogs.txt' was not found")
else:
    print(dog_file.read())

# Question 3
'''
A common problem when prompting for numerical input occurs when providing text 
instead of numbers.  In such a case, when trying to convert the input to int, a
ValueError occurs.  Write a program that prompts the user for two numbers, add
them together and print the result.  Catch the ValueError if either input value is
not a number, and print a friendly error message.  Test your program by entering two
numbers and then by entering some text instead of a number.  
'''
print("Simple Sum of Two numbers!")
try:
    first_number = int(input("First number: "))
    second_number = int(input("Second Number: "))
except ValueError:
    print("Please enter a numerical value")
else:
    print(f"Sum: {first_number + second_number}")

# Question 4
'''
Using the json module write student information to the file in JSON format.  
That is, create a dictionary of of student data in the following format: 
gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}. 

Each dictionary in the list represents one student and contains the keys:
'first_name', 'last_name', 'exam1', 'exam2' and 'exam3'.  The keys map to the
values represengint each student's first name (string), last name (string) and 
three exam scores (integers).  

Output the gradebook_dict in JSON format to the file grades.json.  
'''
import json

output_file = open('grades.json', 'w')
list_d = []
while True:
    line = input("'first_name' 'last_name' 'exam1' 'exam2' 'exam3' (or q to quit)")
    if line == 'q':
        break
    first_name, last_name, exam1, exam2, exam3 = line.split()
    d = {'first_name': first_name, 'last_name': last_name, 'exam1': int(exam1), 'exam2': int(exam2), 'exam3': int(exam3)}
    list_d.append(d)
    
json.dump(list_d, output_file)
output_file.close()
# Question 5
'''
Using the json module to read the grades.json file created in the previous
question.  Display the data in tabular format, including an additional 
column showing each student's average to the right of the student's three
exam grades and an additional row showing the class average on each exam.  
'''