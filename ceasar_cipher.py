def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("Caesar Cipher Program")
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == 'e':
    print("Encrypted Message:", encrypt(message, shift))
elif choice == 'd':
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid choice")

