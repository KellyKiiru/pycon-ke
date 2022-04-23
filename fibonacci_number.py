'''
fibonacci series is a series that is generated by the addition of the two preciding numbers
This is a small application that will determine if the number is a fibonacci number.
This is are the first few digits of the sequence (0,1,1,2,3,5,8,13,21,34...)

'''

from unicodedata import digit
from unittest import result
from math import ceil, sqrt


def print_fibonacci():
    '''
    This will display the fibonacci series upto the number input.'''

    num = int(input("Hi there. Kindly input the number you want to check...\n\n"))

    digit1 = 0
    digit2 = 1
    summation = digit1 + digit2
    
    def fibo_series():
        print("As you can see in the series above...\n")
        
    if num <= 0:
        print("Error: kindly input a value that is greater than 0")
    else:
        for i in range(0, num):
            digit1 = digit2
            digit2 = summation
            summation = digit1 + digit2

            print(summation, end=", ")

        '''
        A number is a fibonacci number if and only if it satisfies the following formula:
        5*(n*n)+4 or 5*(n*n)-4 is a perfect square'''

        # logic to check if num will give a perfect square
        result1 = 5*num*num+4
        result2 = 5*num*num-4
        
        # get the squareroot of the result

        sqrs1 = int(sqrt(result1))
        sqrs2 = int(sqrt(result2))

        # multiply the squareroot to compare it with relevant result

        if sqrs1*sqrs1 == result1 or sqrs2*sqrs2 == result2:
            print('\n')
            fibo_series()
            print(num,"is in the fibonacci sequence")
        else:
            print('\n')
            fibo_series()
            print(num,"is not in the fibonacci series")

print_fibonacci()