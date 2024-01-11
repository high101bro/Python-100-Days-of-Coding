import random

# create a new dictionary from a list
# new_dict = {new_key:new_value for item in list}  # format example
names = ['Daniel', 'Lisa', 'Nathan', 'Kaitlyn', 'Amelia', 'James']
student_grades = {name: (random.randint(50, 100)) for name in names}
print(student_grades)

# create a new dictionary from another dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}  # format example
passing_students = {name: grade for (name, grade) in student_grades.items() if grade > 70}
print(passing_students)

# practice... count the number of letters in each word
string = "What is the Airspeed Velocity of an Unladen Swallow?"
new_dict = {word: len(word) for word in string.split()}
print(new_dict)

# practice... convert temp from C to F
forcast = {
    'Monday': 20,
    'Tuesday': 24,
    'Wednesday': 27,
    'Thursday': 31,
    'Friday': 28,
    'Saturday': 27,
    'Sunday': 29,
}
converted_forcast = {day: (temp * 9 / 5) + 32 for (day, temp) in forcast.items()}
print(converted_forcast)

# How to loop through a pandas dataframe
import pandas

# not working?
# converted_forcast_df = pandas.DataFrame(converted_forcast)
# print(converted_forcast_df)

# for (key, value) in converted_forcast.items():
#     print(key)