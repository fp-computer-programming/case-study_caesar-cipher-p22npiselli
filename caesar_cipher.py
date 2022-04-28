# Nolan Piselli

#imports
from string import ascii_uppercase


#functions
def cipher_key(shift):
     original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]
    
    return dict(zip(original_letters, shifted_letters))
    

def shift_line(line, dict_key):
    new_line = ""
    for letter in line:
        letter == dict[dict_key]
    new_line.append(letter)
    return new_line
    


def encrypt_message(filename, dict_key):
    file = open("encrypted_{0}".format(filename), "w")
    file.write


#main
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)