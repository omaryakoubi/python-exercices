# Question 1 :

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def numbers_divisible_by_7() :
    list = []
    range_of_numbers = range(2000,3201)
    for number in range_of_numbers :
        if (number % 7 == 0) and (number % 5 != 0): 
            list.append(str(number))
    return (','.join(list))


#----------------------------------------#

#----------------------------------------#


# Question 2 :

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def factorial(number) :
    if number == 0:
        return 1
    else :
        return number * factorial(number - 1)


#----------------------------------------#

#----------------------------------------#


# Question 3

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints:
# # In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()

def generate_dictionary(number):
    range_of_numbers = range(1, number + 1)
    storage = {}
    for number in range_of_numbers:
       storage[int(number)] =  int(number * number)
    return storage 


#----------------------------------------#

#----------------------------------------#


# Question 4 :

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

#NEED TO REFACTOR THIS CODE 

def sequence_to_list_and_tuple(*sequence_of_numbers):
    list = []
    for number in sequence_of_numbers:
        list.append(str(number))
    print(list)
    print(tuple(sequence_of_numbers))
    

#----------------------------------------#

#----------------------------------------#


# Question 5 :

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

class User_input_class:
    def __init__(self):
        self.user_input = ""
    
    def get_string(self):
        self.user_input = input('Write here: ')
    
    def print_string(self):
        print (self.user_input.upper())

# test = User_input_class()
# test.get_string()
# test.print_string() 


#----------------------------------------#

#----------------------------------------#


# Question 6 :

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# 
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input. 

#NOT WORKING 

def test(*D):
    C = 50
    H = 30
    return 2 * C * D / H


#----------------------------------------#

#----------------------------------------#


# Question 7

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


#----------------------------------------#

#----------------------------------------#


# Question 8:

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sort_sequence_of_words():
    sequence_of_words = input('please give sequance of words: ').split(',')
    sequence_of_words.sort()
    print(','.join(sequence_of_words))


#----------------------------------------#

#----------------------------------------#


# Question 9:

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def to_upper_case():
    sequence = input('please enter a sequence of characters: ')
    if sequence:
        return (sequence.upper())
    else :
        return 'nothing can be capitalazed no sequence of characters detected!'
    
print(to_upper_case())