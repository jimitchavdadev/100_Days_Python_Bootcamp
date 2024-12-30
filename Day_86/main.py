import tkinter as tk
import random
import time

# List of sample texts for the typing test
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "Practice makes perfect."
]

# Function to start the typing test
def start_test():
    global start_time
    global typing_started
    typing_started = True
    start_button.config(state=tk.DISABLED)
    
    # Select a random text
    text = random.choice(sample_texts)
    text_label.config(text=text)
    typed_text.delete(0, tk.END)
    
    start_time = time.time()  # Record the start time

# Function to check the typing result
def check_result():
    global typing_started
    if not typing_started:
        return
    
    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time  # Calculate the time taken
    typed_text_value = typed_text.get()

    # Calculate the number of words typed
    words = len(typed_text_value.split())
    speed = words / (time_taken / 60)  # Words per minute
    
    # Display result
    result_label.config(text=f"Your typing speed: {speed:.2f} WPM")
    
    # Enable the start button again
    start_button.config(state=tk.NORMAL)
    typing_started = False

# Set up the main Tkinter window
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")

typing_started = False
start_time = 0

# Create and place widgets
instruction_label = tk.Label(root, text="Type the text below as fast as you can!", font=("Arial", 14))
instruction_label.pack(pady=10)

text_label = tk.Label(root, text="", font=("Arial", 16), width=50, height=3, anchor="w", justify="left")
text_label.pack(pady=20)

typed_text = tk.Entry(root, font=("Arial", 14), width=50)
typed_text.pack(pady=10)

check_button = tk.Button(root, text="Check Result", font=("Arial", 14), command=check_result)
check_button.pack(pady=10)

result_label = tk.Label(root, text="Your typing speed will appear here", font=("Arial", 14))
result_label.pack(pady=20)

start_button = tk.Button(root, text="Start Test", font=("Arial", 14), command=start_test)
start_button.pack(pady=10)

# Run the application
root.mainloop()
