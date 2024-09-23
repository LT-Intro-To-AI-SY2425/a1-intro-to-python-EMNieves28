# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

def fibonacci_sequence(n):
    if n < 0: 
        raise ValueError("Input must be a non-negative interger.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n +1):
            a, b = b, a + b
        return b
# example
print(fibonacci_sequence(10)) 
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

assert fibonacci_sequence(3) == 2, "Test case 3 failed"
assert fibonacci_sequence(7) == 13, "Test case 7 failed"

print("All test cases passed :)")

def sum_of_digits(num):
        # Convert the number to string and remove any negative signs
        num_str = str(abs(num))
        total = 0

        for char in num_str:
            total += int(char)

        return total 
    
number = int(input("Enter an integer: "))