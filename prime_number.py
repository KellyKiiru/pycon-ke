#'''
#A python function to check whether a number is a prime number or not'''


import math
import numbers


def is_prime():
    def spacing():
        print("\n")
        
    def if_prime():
        print(f"{number} is a prime number.")
        spacing()
        
    def if_not_prime():
        print (f"From our calculation, {number} is not a prime number")
        spacing()
        
    def start_program():
        print("""Hi there. This is a simple program that calculates and then determines if a number is a prime number or not
        Want to try it out? Type yes...""")
        print('\n')
    
    start_program()

    confirmation = input().lower()
    
    if confirmation == 'yes':

        print("input number to check\n")
        number = int(input())
        
        for i in range(2, number):
            if number%i == 0:
                if_not_prime()
                break
        else:
            if_prime()
        
        
        
is_prime()