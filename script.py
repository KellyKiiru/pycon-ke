#'''
#A python function to check whether a number is a prime number or not'''


import math
import numbers


def is_prime():
    print("""Hi there. This is a simple program that calculates and then determines if a number is a prime number or not
      Want to try it out?""")
    print('\n')
    confirmation = input().lower()

    if confirmation == 'yes':

        print("input number to check\n")
        number = int(input())
        if number % 2 == 0:
            print (f"From our calculation, {number} is not a prime number")
        elif not number % 2 == 0:
            pass

        
        
is_prime()


#def isprime(num):
#    for n in range(2,int(num**0.5)+1):
#        if num%n==0:
#            print(num**0.5)
#            return False
#    return True
#print(isprime(7))
#print(isprime(8))
