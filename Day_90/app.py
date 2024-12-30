import tkinter as tk
from tkinter import messagebox
import time

# Main app class
class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Writing App")
        self.root.geometry("600x400")

        # Create Text widget for typing
        self.text_widget = tk.Text(self.root, wrap="word", font=("Arial", 14), height=15, width=50)
        self.text_widget.pack(pady=20)

        # Label for instructions
        self.instruction_label = tk.Label(self.root, text="Type something. If you stop for 5 seconds, the text will disappear.", font=("Arial", 12))
        self.instruction_label.pack()

        # Variable to store last typing time
        self.last_typed_time = time.time()

        # Bind keypress events to check for typing
        self.text_widget.bind("<KeyPress>", self.on_typing)

        # Start checking for text disappearance
        self.check_for_inactivity()

    def on_typing(self, event):
        """
        Update the last typed time every time the user types a key.
        """
        self.last_typed_time = time.time()

    def check_for_inactivity(self):
        """
        Check if the user has stopped typing for more than 5 seconds.
        If so, clear the text.
        """
        current_time = time.time()

        if current_time - self.last_typed_time > 5:
            self.clear_text()

        # Call this method again after 1 second
        self.root.after(1000, self.check_for_inactivity)

    def clear_text(self):
        """
        Clear the text widget if 5 seconds have passed without typing.
        """
        self.text_widget.delete(1.0, tk.END)
        messagebox.showinfo("Text Cleared", "Your text has been cleared due to inactivity.")

# Initialize the Tkinter window
def main():
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
