import os
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import io

# Initialize Flask application
app = Flask(__name__)

# Directory for uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to extract the most common colors from the image
def get_palette(image_path, num_colors=5):
    # Open image using Pillow
    img = Image.open(image_path)
    img = img.resize((img.width // 5, img.height // 5))  # Resize to speed up processing
    img = img.convert('RGB')
    
    # Convert image into a numpy array
    pixels = np.array(img).reshape(-1, 3)
    
    # Use KMeans clustering to find the most common colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    # Get the colors from the centroids
    colors = kmeans.cluster_centers_.astype(int)
    
    return colors

# Function to display the colors as a palette
def create_palette(colors):
    plt.figure(figsize=(8, 2))
    plt.imshow([colors])
    plt.axis('off')
    plt.tight_layout()

    # Save the color palette as an image
    palette_path = 'static/palette.png'
    plt.savefig(palette_path)
    plt.close()

    return palette_path

# Route to handle the home page and file upload
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the uploaded image and generate the palette
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    # Save the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)
    
    # Get the most common colors from the image
    colors = get_palette(image_path, num_colors=5)
    
    # Create and save the color palette
    palette_path = create_palette(colors)
    
    return render_template('result.html', palette_path=palette_path)

if __name__ == "__main__":
    app.run(debug=True)
