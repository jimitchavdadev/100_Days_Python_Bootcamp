import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

# Function to load an image
def load_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        try:
            image = Image.open(file_path)
            image.thumbnail((600, 600))  # Resize image to fit in window
            img = ImageTk.PhotoImage(image)
            label.config(image=img)
            label.image = img  # Keep a reference to the image
            global img_path
            img_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {e}")

# Function to add watermark
def add_watermark():
    if not img_path:
        messagebox.showwarning("Warning", "No image loaded.")
        return
    
    # Get watermark text from entry box
    watermark_text = watermark_entry.get()
    if not watermark_text:
        messagebox.showwarning("Warning", "Please enter watermark text.")
        return
    
    try:
        # Open the image
        image = Image.open(img_path)
        draw = ImageDraw.Draw(image)
        
        # Use a default font or a specific one
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()

        # Calculate text size and position
        text_width, text_height = draw.textsize(watermark_text, font)
        width, height = image.size
        position = (width - text_width - 10, height - text_height - 10)  # Bottom-right corner

        # Add watermark
        draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white text

        # Save the watermarked image
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if save_path:
            image.save(save_path)
            messagebox.showinfo("Success", "Watermark added and image saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error adding watermark: {e}")

# Set up the main Tkinter window
root = tk.Tk()
root.title("Image Watermarking App")
root.geometry("800x600")

img_path = None  # Global variable to store the image path

# Create and place widgets
label = tk.Label(root, text="No Image Loaded", width=50, height=20)
label.pack(pady=20)

# Button to load an image
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(pady=10)

# Watermark text entry
watermark_label = tk.Label(root, text="Enter Watermark Text:")
watermark_label.pack(pady=5)
watermark_entry = tk.Entry(root, width=40)
watermark_entry.pack(pady=5)

# Button to add watermark
watermark_button = tk.Button(root, text="Add Watermark", command=add_watermark)
watermark_button.pack(pady=10)

# Run the application
root.mainloop()
