alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(txt, shift_number):
    encrypted_message = ""
    splitted_text = [*txt]
    for i in splitted_text:
        item_position = alphabet.index(i)
        encrypted_letter = alphabet[item_position + shift_number]
        encrypted_message += encrypted_letter
    return encrypted_message


def decrypt(txt, shift_number):
    decrypted_message = ""
    splitted_text = [*txt]
    for i in splitted_text:
        item_position = alphabet.index(i)
        decrypted_letter = alphabet[item_position - shift_number]
        decrypted_message += decrypted_letter
    return decrypted_message


if direction == "encode":
    print(f"The encoded text is {encrypt(txt=text, shift_number=shift)}")
elif direction == "decode":
    print(f"The decoded text is {decrypt(txt=text, shift_number=shift)}")
else:
    print(f"{direction} is not an intended comman for this program!")
