import pandas

# Read the CSV file containing the NATO phonetic alphabet
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the CSV file in the format {letter: code}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print("Phonetic Dictionary:")
print(phonetic_dict)


# Function to convert a user-inputted word to phonetic code words
def generate_phonetic():
    try:
        # Get user input and convert it to uppercase
        word = input("Enter a word: ").upper()

        # Generate a list of phonetic code words
        output_list = [phonetic_dict[letter] for letter in word]
        print(f"Phonetic Code Words: {output_list}")
    except KeyError:
        # Handle invalid characters in the input
        print("Sorry, only letters in the alphabet are allowed. Please try again.")
        generate_phonetic()  # Retry on invalid input


# Call the function to generate phonetic code words
generate_phonetic()
