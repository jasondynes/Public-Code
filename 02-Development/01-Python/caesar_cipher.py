logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift_num):
    encrypted_string = ""
    for char in text:
        if char.isalpha():
            char_index = alphabet.index(char)
            # can overflow outside of list hence check
            encrypted_char = alphabet[char_index + shift_num]
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string


def decrypt(text, shift_num):
    decrypted_string = ""
    for char in text:
        if char.isalpha():
            char_index = alphabet.index(char)
            decrypted_char = alphabet[char_index - shift_num]
            decrypted_string += decrypted_char
        else:
            decrypted_string += char
    return decrypted_string


# main program execution
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
try:
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = shift % 25
except ValueError:
    print("That was not a valid number!")
else:
    if direction == "encode":
        output = encrypt(text, shift)
        print(f"Encrypted text is as follows: \n{output}")
    elif direction == "decode":
        output = decrypt(text, shift)
        print(f"Decrypted text is as follows: \n{output}")
    else:
        print("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
