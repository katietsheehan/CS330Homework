
#Due: February 6th at the beginning of class

#Katie Sheehan

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re

solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print (s0 + "\n")

print (solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = "\\d"
if re.search(pattern, s0):
    print ("It starts with 'T'!" + "\n")
else:
    print ("My regex is incorrect, it should detect the 'T'!" + "\n")

print (solution_separator)

# 2) Use a regular expression to decompose the string into words and place those words intp a list.
#    Extract the first word into a variable and print it
pattern = " "
words = re.split(pattern, s0)
print (words)
print ("\n")
first_word = words[0]
print ("The first word is: '" + first_word + "'\n")

print (solution_separator)

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
#
pattern = " "
words = re.split(pattern, s0)
for word in words:
    print (word + "\n")


print (solution_separator)


# 4)
s1 = "Mary was born on September 17, 1986"

# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
pattern = "Mary"
if re.search(pattern, s1):
    print ("this statement contains 'Mary'" + "\n")
else:
    print ("does not contain 'Mary'")
# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
pattern = "\d{4}"
if re.search(pattern, s1):
    print ("this statement contains a four digit number"+ "\n")
else:
    print ("does not contain four digit number")
# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
match = re.search(pattern, s1)
if match:
    b_year = match.group()
    print ("the person was born in " + b_year + "\n")


print (solution_separator)

# 5)
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."

# a) Write a regular expression to match the word "dog", but not the name "Dog"
pattern = r"dog\b"
if re.search(pattern, s2):
    print("Statement contains 'dog' but not 'Dog'" + "\n")
else:
    print("this statement does not contain 'dog'" + "\n")
# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
words = []
match = re.search(pattern, s2)
if match:
    words.append(match.group())
for word in words:
    print (word + "\n")
# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
match = re.findall(pattern, s2, re.IGNORECASE)
if match:
    print("found 'dog' or 'Dog'" + "\n")
else:
    pring("did not find" + "\n")
# d) Write a regular expression to match "dog" or "fog"
pattern = r"[a-z]+og\b"
if re.search(pattern, s2):
    print("Statement contains 'dog' or 'fog'" + "\n")
else:
    print("this statement does not contain 'dog' or 'fog'" + "\n")
# e) Print all outputs.
matches = re.findall(pattern, s2)
for found in matches:
    print (found)

print (solution_separator)

# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
pattern = r"^\d{5}"
match = re.search(pattern, s3)
if match:
    firstnum = match.group()
    print (firstnum + "\n")
# b) Write a regular expression to extract all numbers, store them in an array, then print the array.
pattern = "\d+"
numbers = re.findall(pattern, s3)
for num in numbers:
    print (num +"\n")

print (solution_separator)

# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
pattern = "\s{2,}"
result = re.sub(pattern, "", s4)
print (result)

print (solution_separator)

# 8)
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"

# a) Write a regular expression to print everything from the first "begin" to the last "end".
pattern = "begin.+end"
match = re.search(pattern, s5)
if match:
    print (match.group() + "\n")
# b) Write a regular expression to print only the text from the first "begin" to the first "end"
pattern = r"begin\s\w+\s\w+\s\w+\send\b"
match = re.search(pattern, s5)
if match:
    print(match.group())
# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
arr = []
pattern = r"begin\s(\w+\s(\w+\s){0,2})end"
m = re.findall(pattern, s5)
for item in m:
    match = item[0]
    arr.append(match)
print(arr)

# d) Print all outputs.

print (solution_separator)

# 9)
s6 = "The date 5/17/1982 is trickier to get"

# a) Write a regular expression to extract the date.
pattern = "\d.+\d"
matches = re.findall(pattern, s6)
for match in matches:
    print(match)
# b) Capture the date in a variable f_date
match = re.search(pattern, s6)
if match:
    f_date = match.group()
# c) Split the date and store it as month, day, year
date = re.split("/", f_date)
print (date)
# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
year = date[2]
month = date[0]
day = date[1]
comp_date = year + "-0" + month + "-" + day
# e) Print comp_date
print(comp_date)

print (solution_separator)

# 10) Extra Credit:
s8 = "These are some dates: 1/23/2011, 2/1/2006, 12/31/2007, 9/15/1993, 04/23/1797."

# a) Use a regex to collect the dates into a list
# b) Use the code above to convert them into yyyy-mm-dd format.
# c) Print the dates in chronological order

print (solution_separator)
