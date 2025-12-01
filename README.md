# Invisible-Cloak

Invisible Black Cloak – OpenCV Project

A simple invisibility cloak effect built using Python and OpenCV.
The program detects pure black cloth in video frames and replaces the cloth area with a captured background, creating an illusion of invisibility.

📌 How It Works

The camera first captures a clean background without the user.

In each frame, the program detects black cloth using color + light-based filters.

The detected region is replaced with the background, making the cloak appear invisible.

📂 Functions Explained
1. capture_background(cap, num_frames=40)

Captures multiple frames of the background and computes the median of all frames.
This produces a clean, stable background image without noise.

Purpose:
✔ Helps in creating the invisibility effect
✔ Removes flicker by using many frames
✔ Ensures background is steady even with slight camera noise

2. generate_black_cloak_mask(frame)

Creates a mask of the black cloth so the program knows which area to hide.

This function uses multiple techniques:

HSV strict black range
Detects very dark colors precisely.

LAB L-channel thresholding
Identifies dark regions even under shadows.

Edge suppression
Removes thin edges (hair, beard, objects) so they don’t trigger false detection.

Noise removal & smoothing
Uses bilateral filter, Gaussian blur, and morphological operations to produce a clean mask.

Purpose:
✔ Detect black cloak accurately
✔ Avoid false positives
✔ Keep cloak shape stable even with folds and wrinkles

3. apply_invisibility_effect(frame, mask, background)

Applies the invisibility effect by blending:

The visible part of the frame

The background inside the cloak area

Steps:

Softens mask with Gaussian blur (smooth edges)

Inverts mask to keep non-cloak areas visible

Replaces cloak area with background

Purpose:
✔ Makes cloak disappear
✔ Smooth & clean visual output

4. main()

Controls the entire program:

Opens the webcam

Captures the background using capture_background()

Continuously reads camera frames

Generates cloak mask using generate_black_cloak_mask()

Applies invisibility using apply_invisibility_effect()

Displays final output

Quits on pressing Q

▶️ Running the Program

Make sure dependencies are installed:

pip install opencv-python numpy


Run:

python main.py
