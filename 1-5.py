#1 Write a program to check whether a number is even or odd.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
number = 5
print(check_even_odd(number))

#2 Write a program to check whether a number is prime or not.

def check_prime(number):
    if number == 1:
        return "Not a prime number"
    elif number == 2:
        return "Prime number"
    else:
        for i in range(2, number):
            if number % i == 0:
                return "Not a prime number"
        return "Prime number"
    
# Example usage:    
number = 5
print(check_prime(number))

#3 Write a program to find the factorial of a number.   

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)   
    
# Example usage:
number = 5
print(factorial(number))

#4 Write a program to generate the Fibonacci series.

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
    
# Example usage:
number = 10
print(fibonacci(number))

def generate_fibonacci(limit):
    fs = [0, 1]
    while True:
        next_number = fs[-1] + fs[-2]
        if next_number > limit:
            break
        fs.append(next_number)
    return fs

# Example usage:
limit = 10
print(generate_fibonacci(limit))

#5 Write a program to find the sum of all the digits of a number.

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    return sum

# Example usage:
number = 12345
print(sum_of_digits(number))
