# Question 1
'''
From your accounts.txt file (from last class) read each line and create 
a dictionary of dictionaries.  The outer dictionary key is the account 
number.  The inner dictionary key is the last name and the value in 
the inner dictionary is the balance.  Print the final dictionary.  
'''

# Question 2
'''
(a) Open a file called grades.txt for writing that will hold student 
    grade information.  This information will be read from the user.  
    Each input line given by the user is of the form: 
    firstname, lastname, exam1grade, exam2grade, exam3grade.  
    Read grade information for 10 students and write that information 
    to your grades.txt file.  Make sure to close the file after 
    writing to it.  

(b) Once your grades.txt file is populated, read and store the infomration
    from the file.  Determine what data structure (e.g. lists, dictionaries, 
    sets, etc.) would best suit for storing the data in the file.  Once 
    your data is stored, compute the following: 
    (i) the minimum, maximum and average of exam1grade, exam2grade, exame3grade
        for each student and print this information
    (ii) the minimum, maximum and average of exam1grade across all students.
         Do this for exam2grade and exam3grade as well.  
    (iii) the average of the average of all 3 exams for all students.  
'''

#a)
output_file = open('grades.txt', 'w')
for i in range(2):
    firstname, lastname, exam1grade, exam2grade, exam3grade, = input().split()
    output_file.write(firstname + ',' + lastname + ',' + exam1grade + ',' + exam2grade + ',' + exam3grade + '\n')
output_file.close()

output_file = open('grades.txt', 'r')
grade_d = {}
for line in output_file:
    firstname, lastname, exam1grade, exam2grade, exam3grade = line.split(',')
    grade_d[(firstname, lastname)] = [int(exam1grade), int(exam2grade), int(exam3grade)]

#b)
#i) ii) iii)
mins = [min([value[i] for value in list(grade_d.values())]) for i in range(3)]
maxes = [max([value[i] for value in list(grade_d.values())]) for i in range(3)]
averages_eachexam = [sum([value[i] for value in list(grade_d.values())])/len(grade_d) for i in range(3)]
averages_eachperson = [(person, sum(grade_d[person])/3) for person in grade_d]

print(f"Mins: {mins}")
print(f"Maxes: {maxes}")
print(f"Average per exam: {averages_eachexam}")
print(f"Individual averages {averages_eachperson}")
  
# Question 3
'''
Download into your folder the words.txt file on Lea.  You will notice that each
word in the words.txt file is on a new line.  
(a) Open a new file called words_updated.txt with writing mode, and write all the
    words from the words.txt file continuously one after the other only separated
    by a space.  Make sure that you strip all the white space after each word
    that you read from the words.txt file.  Once you are done, make sure you
    close all files that you had opened.  

(b) Create an integer num_words that will hold the number of words that you have
    in your words_updated.txt (or words.txt) file.  Now prompt the user to read
    an integer k (between 1 and 80) from the user.  Make sure to do input 
    validation so to be assured that the user abides the constraints on k.  

    Open a new file called result.txt with writing mode, and read the words 
    from your words_updated.txt file and write them in result.txt such that
    the number of characters on each line of result.txt is at most k (not
    counting the spaces between the words).  That is, if the next word 
    begin considered fits on the current line, add it to the current line
    (make sure to include a space between each pair of words on the line). 
    Otherwise, put this word on a new line (which will become the new
    current line).

    One you finish writing to your result.txt file, print the content of
    your file.  Make sure to close all files that you have opened.  
'''
#a)
read_file = open('words.txt', 'r')
write_file = open('words_updated.txt', 'w')

for line in read_file:
    write_file.write(line.split('\n')[0] + ' ')

read_file.close()
write_file.close()

#b)
read_file = open('words_updated.txt', 'r')
write_file = open('results.txt', 'w')

k = -1
while 80 < k or k < 1:
    k = int(input("Value of k: "))

line_count = 0
for line in read_file:
    words = line.split()
    for word in words:
        if line_count + len(word) <= k:
            line_count += len(word)
            write_file.write(word + ' ')
        else:
            line_count = len(word)
            write_file.write('\n' + word)

read_file.close()
write_file.close()

 