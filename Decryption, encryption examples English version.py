def hidden_message_generator(text):
    hidden_message = ""
    for char in text:
        encrypted_char = chr(ord(char) + 1)
        hidden_message += encrypted_char
        print(f"Encryption: '{char}' -> '{encrypted_char}'")
    return hidden_message

def decrypt_message(hidden_message):
    decrypted_message = ""
    for char in hidden_message:
        decrypted_char = chr(ord(char) - 1)
        decrypted_message += decrypted_char
        print(f"Decrypted: '{char}' -> '{decrypted_char}'")
    return decrypted_message

text = input("Please enter the message you want to hide: ")
hidden = hidden_message_generator(text)
print("Hidden message:", hidden)

decrypted = decrypt_message(hidden)
print("Decrypted message:", decrypted)
