#Quetion 1;
print("Hello, world!")
print("=============================================")
#================================================================================

#Quetion 2
integer_var = 10

float_var = 3.14

string_var = "Hello, World!"

boolean_var = True

list_var = [1, 2, 3, 4, 5]

tuple_var = (6, 7, 8, 9, 10)

dictionary_var = {"name": "John", "age": 25, "city": "New York"}

set_var = {1, 2, 3, 4, 5}

print("Type of integer_var:", type(integer_var), ", value:", integer_var)
print("Type of float_var:", type(float_var), ", value:", float_var)
print("Type of string_var:", type(string_var), ", value:", string_var)
print("Type of boolean_var:", type(boolean_var), ", value:", boolean_var)
print("Type of list_var:", type(list_var), ", value:", list_var)
print("Type of tuple_var:", type(tuple_var), ", value:", tuple_var)
print("Type of dictionary_var:", type(dictionary_var), ", value:", dictionary_var)
print("Type of set_var:", type(set_var), ", value:", set_var)
print("=============================================")
#==================================================================================

#Quetion 3
numbers = list(range(1, 11))
print("Original list:", numbers)

numbers.append(20)
print("After adding 20:", numbers)

numbers.remove(3)
print("After removing 3:", numbers)

numbers.sort()
print("Sorted list:", numbers)
print("=============================================")
#====================================================================================

#Quetion 4
numbers = [10, 20, 30, 40]

sum_numbers = sum(numbers)

average = sum_numbers / len(numbers)

print("Sum:", sum_numbers)
print("Average:", average)
print("=============================================")
#===================================================================================

#Quetions 5
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

input_str = "Python"
reversed_str = reverse_string(input_str)
print(reversed_str)
print("=============================================")
#===================================================================================


#Quetions 6
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Test the program
input_str = "Hello"
vowel_count = count_vowels(input_str)
print("Number of vowels:", vowel_count)
print("=============================================")
#===================================================================================

#Quetions 7
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
input_num = 13
if is_prime(input_num):
    print(input_num, "is a prime number.")
else:
    print(input_num, "is not a prime number.")
    print("=============================================")
#===================================================================================

#Quetions 8
def factorial(number):
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

# Test the function
input_num = 5
factorial_num = factorial(input_num)
if factorial_num is None:
    print("Cannot calculate factorial for a negative number.")
else:
    print("Factorial of", input_num, "is", factorial_num, ".")
    print("=============================================")
#===================================================================================

#Quetions 9
def generate_fibonacci(n):
    fibonacci_sequence = []
    if n >= 1:
        fibonacci_sequence.append(0)
    if n >= 2:
        fibonacci_sequence.append(1)
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return fibonacci_sequence

input_num = 5
fibonacci_sequence = generate_fibonacci(input_num)
print(fibonacci_sequence)
print("=============================================")
#===================================================================================

#Quetions 10
squares = [x ** 2 for x in range(1, 11)]
print(squares)
print("=============================================")
#===================================================================================



