# Dictionary to map each character to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Function to convert string to Morse code
def text_to_morse(text):
    # Convert the text to uppercase and remove unwanted characters (e.g., numbers, punctuation)
    text = text.upper()
    morse_code = []
    
    for char in text:
        if char == " ":
            morse_code.append(" ")  # Add space between words
        elif char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append("")  # For any unsupported character
    
    return " ".join(morse_code)

# Function to get user input and convert it
def main():
    text = input("Enter the text to convert to Morse Code: ")
    morse_code = text_to_morse(text)
    print("Morse Code:", morse_code)

if __name__ == "__main__":
    main()
