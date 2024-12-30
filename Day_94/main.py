import pyautogui
import numpy as np
import cv2
import time
import mss

# Coordinates for the dinosaur (you may need to adjust this based on your screen size)
dino_position = (100, 300)  # X, Y for where the dinosaur's feet are

# Screen capture region (you can adjust these coordinates based on your game window)
screen_region = {"top": 200, "left": 0, "width": 800, "height": 400}  # Capture the area where obstacles appear

# Function to detect obstacles (Cacti or Birds)
def detect_obstacle(screen):
    # Convert the image to grayscale
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    
    # Threshold the image to highlight dark objects (like cacti or birds)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours of the obstacles
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # If contours are detected, it means there's an obstacle
    if len(contours) > 0:
        return True
    return False

# Function to simulate a jump (press spacebar)
def jump():
    pyautogui.press('space')

# Main loop to keep checking for obstacles and jumping
def play_game():
    print("Starting the game in 3 seconds... Make sure the game is in focus!")
    time.sleep(3)  # Give a few seconds to focus on the game window

    with mss.mss() as sct:
        while True:
            # Take a screenshot of the game region
            screenshot = np.array(sct.grab(screen_region))
            
            # Convert RGB to BGR (OpenCV uses BGR)
            screen = cv2.cvtColor(screenshot, cv2.COLOR_RGBA2BGR)
            
            # Detect obstacle in the game screen
            if detect_obstacle(screen):
                print("Obstacle detected! Jumping...")
                jump()
            
            # Sleep for a short time before checking again
            time.sleep(0.1)

# Run the game automation
if __name__ == "__main__":
    play_game()
