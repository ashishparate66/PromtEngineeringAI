
#Quetion 1;
n = 5  
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
    print("=============================================")
#================================================================================


#Quetion 2;
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0:
        if num > 150:
            continue
        elif num > 500:
            break
        print(num)
print("=============================================")
#================================================================================


#Quetion 3;
s1 = "Ault"
s2 = "Kelly"
mid_index = len(s1) // 2  
s3 = s1[:mid_index] + s2 + s1[mid_index:]  
print(s3)
print("=============================================")
#================================================================================


#Quetion 4;
str1 = "PyNaTive"

lowercase_letters = ""
uppercase_letters = ""

for char in str1:
    if char.islower():
        lowercase_letters += char
    else:
        uppercase_letters += char

arranged_str = lowercase_letters + uppercase_letters

print(arranged_str)
print("=============================================")
#================================================================================


#Quetion 5;
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = []

min_len = min(len(list1), len(list2))

for i in range(min_len):
    result.append(list1[i] + list2[i])

result.extend(list1[min_len:])
result.extend(list2[min_len:])

print(result)
print("=============================================")
#================================================================================


#Quetion 6;
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]

print(result)
print("=============================================")
#================================================================================


#Quetion 7;
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)
    print("=============================================")
#================================================================================


#Quetion 8;
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = {}

for name in employees:
    result[name] = defaults

print(result)
print("=============================================")
#================================================================================


#Quetion 9;
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

result = {}

for key in keys:
    if key in sample_dict:
        result[key] = sample_dict[key]

print(result)
print("=============================================")
#================================================================================


#Quetion 10;
tuple1 = (11, [22, 33], 44, 55)

list1 = list(tuple1)
list1[1][0] = 222

tuple1 = tuple(list1)

print("tuple1:", tuple1)
print("=============================================")
#================================================================================
