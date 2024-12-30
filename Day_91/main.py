import pyttsx3
import PyPDF2

# Function to read the PDF and extract text
def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to convert text to speech
def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties (optional)
    rate = engine.getProperty('rate')  # Current speech rate
    engine.setProperty('rate', rate-50)  # Decrease speech rate for clarity
    
    volume = engine.getProperty('volume')  # Current volume
    engine.setProperty('volume', volume+0.25)  # Increase volume

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    # Input PDF file path
    pdf_path = input("Enter the path to the PDF file: ")

    # Extract text from PDF
    text = pdf_to_text(pdf_path)
    
    # Check if text extraction was successful
    if not text:
        print("No text found in the PDF. It might be an image-based PDF.")
        return

    # Convert extracted text to speech
    print("Converting PDF to speech...")
    text_to_speech(text)
    print("Speech conversion completed!")

if __name__ == "__main__":
    main()
