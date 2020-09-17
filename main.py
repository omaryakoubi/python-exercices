# Question 1 :
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def numbers_divisible_by_7() :
    list = []
    range_of_numbers = range(1999,3201)
    for number in range_of_numbers :
        if (number % 7 == 0) and (number % 5 != 0): 
            list.append(str(number))
            print(','.join(list))


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

