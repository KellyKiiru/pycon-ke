#'''
#A python function to check whether a number is a prime number or not'''


import math
import numbers


def is_prime():
    def start_program():
        print("""Hi there. This is a simple program that calculates and then determines if a number is a prime number or not
        Want to try it out? Type yes...""")
        print('\n')
    
    start_program()
    
    def spacing():
        print("\n")
        
    confirmation = input().lower()
    
    def if_prime():
        print(f"{number} is a prime number.")
        spacing()
        
    def if_not_prime():
        print (f"From our calculation, {number} is not a prime number")
        spacing()

    if confirmation == 'yes':

        print("input number to check\n")
        number = int(input())
        if number % 2 == 0 and number % 1 == 0 and number > 0 and number % number == 0 :
            print(number)
            print('\n')
            if_not_prime()
        elif number <0:
            print("Please input numbers greater than 1")
        else:
            if_prime()
            #start_program()
    else:
        print("Want to start again? If yes click 'Enter'")
        
        start_program()
        
        
is_prime()


#def isprime(num):
#    for n in range(2,int(num**0.5)+1):
#        if num%n==0:
#            print(num**0.5)
#            return False
#    return True
#print(isprime(7))
#print(isprime(8))
