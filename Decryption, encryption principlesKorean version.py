def hidden_message_generator(text):
    hidden_message = ""
    for char in text:
        encrypted_char = chr(ord(char) + 1)
        hidden_message += encrypted_char
        print(f"암호화: '{char}' -> '{encrypted_char}'")
    return hidden_message

def decrypt_message(hidden_message):
    decrypted_message = ""
    for char in hidden_message:
        decrypted_char = chr(ord(char) - 1)
        decrypted_message += decrypted_char
        print(f"복호화: '{char}' -> '{decrypted_char}'")
    return decrypted_message

text = input("숨길 메시지를 입력하세요: ")
hidden = hidden_message_generator(text)
print("숨겨진 메시지:", hidden)

decrypted = decrypt_message(hidden)
print("복호화된 메시지:", decrypted)
