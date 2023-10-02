"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

#store the values after running the function
cache=[]

def primes(number_of_primes):
    list = []


    if number_of_primes == 0 or number_of_primes < 0:
        raise ValueError("Number of primes must be a positive integer")

    # Start with a range of numbers to check
    num = 2
    while len(list) < number_of_primes:
        # Check if num is in the cache and is prime
        if num in cache:
            list.append(num)
        elif is_prime(num):
            list.append(num)
            cache.append(num)  # Add num to the cache
        num += 1
    
    return list


    
    return list


def is_prime(number):

    #return true or false based on the if clauses 
    #find if a number if prime or not

    #the number cant be less than 1 

    #the number cant be even so check %2 

    #and then try to divide the number to all the odd numbers that comes before it 
    #if its not , then it is a prime.

    #the number can be 2

    if number<1:
        return False
    if number ==2:
        return True
    if number %2 ==0 :
        return False
    
    #find odd  number range
    for oddNumber in range(3,int(number**0.5) + 1, 2):
        if(number%oddNumber==0):
            return False
    return True
        


print(primes(10)) 