userNo = int(input("Enter a number to check whether its a prime no or not"))

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime=False
    if is_prime:
        print("it's a prime number")
    else:
        print("it's not a prime number")

prime_checker(number=userNo)