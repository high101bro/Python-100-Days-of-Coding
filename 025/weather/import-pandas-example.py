#! /usr/bin/env python3

# with open('weather.csv', 'r') as file:
#     data = file.readlines()
#
# print(data)

import pandas

data = pandas.read_csv("weather.csv")

# show all csv file
print(data)
# shows pandas dataframe object
print(type(data))


# show all data in a column
print(data['temp'])
# hows pandas series object
print(type(data['temp']))

# grab first item
print(data['temp'][0])
# this is also a pandas series
print(data['temp'][0])

# you can convert csv to dictionary, as well as many other formats
data_dict = data.to_dict()
print(data_dict)
print(type(data_dict))

data_list = data['temp'].to_list()
print(data_list)
print(type(data_list))

# mean value
print(sum(data_list) / len(data_list))
print(data['temp'].mean())

# max value
print(data['temp'].max())

# aside from using the square bracket method, you can call columns headers directly with dot notation
print(data['condition'])
# vs
print(data.condition)


# you can even do search features
print(data[data.day == 'Monday'])
print(data[data.condition == 'Sunny'])

# grab the day with the max temp
print(
    data[data.temp == data.temp.max()]
)

# Create a dataframe from scratch
new_dict = {
    'students': ['Daniel', 'Mark', 'John'],
    'scores': [97, 72, 84]
}
print(new_dict)
df = pandas.DataFrame(new_dict)
print(df)
df.to_csv('pandas_to_csv.csv')



