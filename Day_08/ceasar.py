choice = input("Encode or decode?: ").lower()

def ceasar(text, key, encode=True):
    result = []
    for i in text:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            shift = key if encode else -key
            shifted = chr((ord(i) - base + shift) % 26 + base)
            result.append(shifted)
        else:
            result.append(i)  # Preserve spaces and other characters
    return "".join(result)

if choice == "encode":
    plain = input("Enter the plaintext: ")
    key = int(input("Enter the shift value: "))
    encrypted = ceasar(plain, key, encode=True)
    print(f"The encrypted text is: {encrypted}")

elif choice == "decode":
    cipher = input("Enter the ciphertext: ")
    key = int(input("Enter the shift value: "))
    decrypted = ceasar(cipher, key, encode=False)
    print(f"The decrypted text is: {decrypted}")

else:
    print("Invalid choice. Please choose 'encode' or 'decode'.")
