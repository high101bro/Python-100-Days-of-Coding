
# # Will produce error
# with open('file-does-not-exist.txt', 'r') as file:
#     file.read()
#
# print('does not print')
#
# Traceback (most recent call last):
#   File "C:\Users\danie\Documents\GitHub\Python-100-Days-of-Coding\030\lecture\errors-exceptions.py", line 4, in <module>
#     with open('file-does-not-exist.txt', 'r') as file:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'file-does-not-exist.txt'

##################################################
# # KeyError
# dict = {'key': 'value'}
# print(dict['not-key'])
#
# Traceback (most recent call last):
#   File "C:\Users\danie\Documents\GitHub\Python-100-Days-of-Coding\030\lecture\errors-exceptions.py", line 12, in <module>
#     print(dict['not-key'])
#           ~~~~^^^^^^^^^^^
# KeyError: 'not-key'

##################################################
# # Index Errror
# abc = ['a','b','c']
# abc[3]
#
# Traceback (most recent call last):
#   File "C:\Users\danie\Documents\GitHub\Python-100-Days-of-Coding\030\lecture\errors-exceptions.py", line 29, in <module>
#     abc[3]
#     ~~~^^^
# IndexError: list index out of range

##################################################
# # TypeError
# text = 'abc'
# print(text + 5)
#
# Traceback (most recent call last):
#   File "C:\Users\danie\Documents\GitHub\Python-100-Days-of-Coding\030\lecture\errors-exceptions.py", line 40, in <module>
#     print(text + 5)
#           ~~~~~^~~
# TypeError: can only concatenate str (not "int") to str

##################################################

# # Description
# try:      # something that might cause an exception
#     pass
# except:   # do this if there was an exception
#     pass
# else:     # do this if there were no exceptions
#     pass
# finally:  # do this not matter what happens
#     pass

##################################################
# Big example
# try:
#     file = open('a_file.txt')
#     print(file.readlines())
#     a_dict = {'key': 'value'}
#     # print(a_dict['not-key'])  # COMMENTED OUT TO TEST THE ESLSE
# except FileNotFoundError:
#     print('file created')
#     file = open('a_file.txt', 'w')
#     file.write("new file")
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# except:
#     print('except')
#     print('catch all')
# else:
#     print('else')
#     content = file.read()
#     print(content)
# finally:
#     print('file was closed')
#     file.close()
#
#     # raise KeyError
#     raise TypeError("This is an error I made up")

##################################################
# Raise indepth

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)


##################################################



##################################################
