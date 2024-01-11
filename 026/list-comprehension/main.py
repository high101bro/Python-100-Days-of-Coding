
# Long format
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)


# List comprehension method
# new_list =[new_item for item in list]  # general format
new_list = [n + 1 for n in numbers]
print(new_list)

# Can also do with strings
name = "Komnick"
new_list = [letter for letter in name]
print(new_list)
# Result:
# new_list = ['K', 'o', 'm', 'n', 'i', 'c', 'k']


new_list = [number * 2 for number in  range(1, 6)]
print(new_list)

# Conditional List comprehension
#new_list = [new_item for item in list if test]  # general format
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) < 5]
print(short_names)

# practice... should only give even numbers provided I input a list of 1,2,3,4,5,6,7,...etc
# list_of_strings = input('Enter a comma separated list of numbers: ').split(',')
# numbers = [num for num in list_of_strings if int(num) % 2 == 0]
# print(numbers)


# practice... find out which numbers are in both lists
list_1 = [1,4,6,9,13,16,19,23,27,34,36,41,44,47,52,53,58,5,9,60,62,65,68,69,70,71,72,73,77,79,80,88,92,96,99]
list_2 = [1,5,8,9,10,13,17,19,22,26,29,33,36,39,44,45,46,47,49,51,56,59,60,61,64,68,72,75,78,80,82,85,88,89,91,94,98,99]
same_numbers = [num for num in list_1 if num in list_2]
print(same_numbers)


