# Invisible-Cloak

Invisible Cloak using OpenCV – Aqua/Mint Cloth Detection

A simple invisibility cloak effect built using Python and OpenCV, where the program detects a mint/aqua-colored cloth and replaces that region with the pre-captured background — creating a clean and fun invisibility illusion.

📌 How It Works
1️⃣ Background Capture

At the beginning, the program captures several frames without the user to build a clean background.
This background later replaces the cloak region to create the invisibility effect.

2️⃣ Color-Based Cloak Detection

The system works by detecting a specific mint–aqua color range in each video frame.
It uses simple but effective HSV color thresholding, along with blur and morphological operations to clean noise.

3️⃣ Replacing the Cloak With Background

Wherever the cloth is detected, the pixel area is replaced by the previously captured background frame — making it appear as if the cloth (and whatever is behind it) has vanished.

📂 Functions / Logic Explained
🔹 Background Capture

A loop captures ~30 frames and stores the last one as the stable background.

🔹 Mint–Aqua Cloth Mask

Converts frame to HSV

Applies Gaussian blur to soften edges

Uses two HSV ranges to detect:

Standard mint-aqua tones

Lighter mint variations

Combines both masks

Removes noise using morphological opening

🔹 Invisibility Effect

Detected cloak pixels are replaced:

frame[cloak_mask == 255] = background[cloak_mask == 255]

🔹 Final Display

The processed frame is shown in real time.
Press ESC to exit.

▶️ Running the Program

Install dependencies:

pip install opencv-python numpy


Run the script:

python main.py


Technologies Used:

Python

OpenCV (cv2)

NumPy

HSV Image Processing

Background Substitution

python main.py
