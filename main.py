import cv2
import numpy as np
import time

print("""
     Your cloak is loading....
     Hide from your webcam for the first 5 seconds, 
     as it captures the background (without you in it)
""")

# Initialize webcam
video = cv2.VideoCapture(0)
time.sleep(3)

# Capture background
bg_frame = 0
for _ in range(30):
    success, bg_frame = video.read()

# Flip for mirror effect
bg_frame = np.flip(bg_frame, axis=1)

while video.isOpened():
    success, frame = video.read()
    if not success:
        break

    frame = np.flip(frame, axis=1)

    # Convert to HSV
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blurred_hsv = cv2.GaussianBlur(hsv_img, (35, 35), 0)

    # =============================================
    #           AQUA / MINT COLOR MASK
    # =============================================
    # Main mint-aqua range
    mint_lower_1 = np.array([85, 60, 60])
    mint_upper_1 = np.array([100, 255, 255])

    # Slightly lighter mint tones
    mint_lower_2 = np.array([75, 40, 50])
    mint_upper_2 = np.array([85, 255, 255])

    # Generate masks
    mask1 = cv2.inRange(blurred_hsv, mint_lower_1, mint_upper_1)
    mask2 = cv2.inRange(blurred_hsv, mint_lower_2, mint_upper_2)

    full_mask = mask1 + mask2

    # Clean noise
    full_mask = cv2.morphologyEx(
        full_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)
    )

    # Replace cloak with background
    frame[np.where(full_mask == 255)] = bg_frame[np.where(full_mask == 255)]

    # Display output
    cv2.imshow('Magic Window', frame)

    # ESC key to exit
    if cv2.waitKey(10) == 27:
        break

video.release()
cv2.destroyAllWindows()