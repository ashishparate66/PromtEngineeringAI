#Quetion 1;
people = [("John", 25), ("Jane", 30)]

for name, age in people:
    print(f"{name} is {age} years old.")

print("=============================================")
#================================================================================

#Quetion 2;
def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age
    else:
        print(f"Name '{name}' not found in the dictionary.")

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]
    else:
        print(f"Name '{name}' not found in the dictionary.")

people = {}

add_person(people, "John", 25)
print(people)

update_age(people, "John", 26)
print(people)

delete_person(people, "John")
print(people)
print("=============================================")
#================================================================================

#Quetion 3;
def two_sum(nums, target):
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complement_dict:
            return [complement_dict[complement], i]

        complement_dict[num] = i

    return []

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)
print("=============================================")
#================================================================================

#Quetion 4;
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    reversed_word = word[::-1]

    if word == reversed_word:
        return f"The word '{word}' is a palindrome."
    else:
        return f"The word '{word}' is not a palindrome."

word = "madam"
result = is_palindrome(word)
print(result)
print("=============================================")
#================================================================================

#Quetion 5;
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
print("=============================================")
#================================================================================

#Quetion 6;
from queue import Queue
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q2.put(item)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            return None
        return self.q1.get()
    
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop()) 
stack.push(3)
print(stack.pop()) 
print(stack.pop()) 
print("=============================================")
#================================================================================

#Quetion 7;
output=[]
for num in range(1,100):
    if num%3==0 and num %5==0:
        output.append("FizzBuzz")
    elif num%3==0:
        output.append("Fizz")
    elif num%5==0:
        output.append("Buzz")
    else :
      output.append(str(num))
      print(", ".join(output))
print("=============================================")
#================================================================================

#Quetion 8;
def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    word_count = len(text.split())

    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

input_file = "input.txt"
output_file = "output.txt"
count_words(input_file, output_file)
print("=============================================")
#================================================================================

#Quetion 9;
def divide(n1, n2):
    try:
        result = n1/n2
        return result
    except ZeroDivisionError:
        return "Cannot divided by Zero"
    
n1=10
n2=0
ans = divide(n1,n2)
print(ans)
print("=============================================")
#================================================================================


