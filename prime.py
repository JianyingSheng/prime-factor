"""
prime.py
using pytest -s to input the number
"""
#Number = int(input(" Please Enter any Number: "))

def generate_prime_factors(number_input):
    """
    function that gives the prime factors of input number,
    and raises ValueError when the input number is not an integer
    """
    prime_factors = []
    if not isinstance(number_input,int):
        raise ValueError
    if isinstance(number_input,int):
        if number_input < 1:
            print("A positive integer is expected")
        if number_input > 1:
            i = 2
            while i * i <= number_input:
                if number_input % i == 0:
                    number_input //= i
                    prime_factors.append(i)
                else:
                    i += 1
            if number_input > 1:
                prime_factors.append(number_input)
            if prime_factors == []:
                prime_factors.append(number_input)
    return prime_factors

#print ("The prime factors of " + str(Number) + " is a list of following:")
#print (generate_prime_factors(Number))
