import cv2
import numpy as np

def zoom_image(img, zoom_factor, center_x, center_y):
    if center_x < 0 or center_x > 1 or center_y < 0 or center_y > 1:
        raise ValueError("Coordinates (center_x, center_y) should be in the range from 0 to 1.")

    # Get image dimensions
    height, width = img.shape[:2]

    # Calculate the new zoomed dimensions
    new_width = int(width / zoom_factor)
    new_height = int(height / zoom_factor)

    # Calculate the coordinates for cropping
    start_x = int(center_x * width - new_width / 2)
    start_y = int(center_y * height - new_height / 2)
    end_x = start_x + new_width
    end_y = start_y + new_height

    # Ensure the cropped region stays within the image boundaries
    start_x = max(0, start_x)
    start_y = max(0, start_y)
    end_x = min(width, end_x)
    end_y = min(height, end_y)

    # Crop the image
    cropped_img = img[start_y:end_y, start_x:end_x]

    # Resize the cropped region to the original size
    zoomed_img = cv2.resize(cropped_img, (width, height), interpolation=cv2.INTER_AREA)

    return zoomed_img
