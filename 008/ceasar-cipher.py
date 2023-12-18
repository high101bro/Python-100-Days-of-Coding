#! /usr/bin/env python3

alphabet = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')

# print(alphabet)
print(alphabet.index('m'))

type = input(f"Type 'encrypt' to encrypt, type 'decrypt' to decrypt: ")
text = input(f"Type in your message: ").lower()
shift = int(input('Type in the shift number: '))

def ceasar(text,shift, type):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if type == 'encrypt':
            new_position = position + shift
        elif type == 'decrypt':
            new_position = position - shift
        new_letter = alphabet[new_position]
        new_text += new_letter        
    return new_text


print(
    ceasar(text,shift, type)
)

# def encrypt(text,shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     return cipher_text


# def decrypt(text,shift):
#     plain_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     return plain_text
    
# if type == 'encrypt':
#     print(
#         encrypt(text,shift)
#     )
# elif type == 'decrypt':
#     print(
#         decrypt(text, shift)
#     )
