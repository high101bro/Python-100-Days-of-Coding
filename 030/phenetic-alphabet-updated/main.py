
import pandas

phonetic_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

print(phonetic_alphabet)

print(phonetic_alphabet.to_dict())

phonetic_dict = {row.letter: row.code for (index, row) in phonetic_alphabet.iterrows()}
print(phonetic_dict)

while True:
    user_input = input('Enter a word: ')
    try:
        phonetic_output = [phonetic_dict[letter] for letter in user_input.upper()]
        print(' '.join(phonetic_output))
    except KeyError as error:
        print(f"{error} is not allowed")











