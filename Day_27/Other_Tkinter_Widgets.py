from tkinter import *

# Creating a new window and configuring its properties
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Label
label = Label(text="This is old text")
label.config(text="This is new text")  # Updating label text
label.pack()

# Button
def action():
    print("Button clicked!")

# Calls the action() function when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entry
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")  # Adding default text
print(f"Initial Entry Text: {entry.get()}")  # Printing the default text
entry.pack()

# Text
text = Text(height=5, width=30)
text.focus()  # Puts cursor in the textbox
text.insert(END, "Example of multi-line text entry.")  # Adding default text
print(f"Initial Text Widget Content: {text.get('1.0', END)}")  # Printing the text content
text.pack()

# Spinbox
def spinbox_used():
    print(f"Spinbox Value: {spinbox.get()}")  # Prints the current value in the spinbox

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(f"Scale Value: {value}")  # Prints the current value of the scale

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    print(f"Checkbutton State: {checked_state.get()}")  # Prints 1 if checked, otherwise 0

checked_state = IntVar()  # Variable to hold the state (0 or 1)
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

# Radiobutton
def radio_used():
    print(f"Selected Radio Button: {radio_state.get()}")  # Prints the selected option value

radio_state = IntVar()  # Variable to hold the value of the selected radio button
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    # Prints the currently selected item from the listbox
    try:
        print(f"Selected Item: {listbox.get(listbox.curselection())}")
    except TclError:
        print("No item selected.")

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for index, item in enumerate(fruits):
    listbox.insert(index, item)  # Adding items to the listbox
listbox.bind("<<ListboxSelect>>", listbox_used)  # Binding selection event
listbox.pack()

# Starting the Tkinter event loop
window.mainloop()
