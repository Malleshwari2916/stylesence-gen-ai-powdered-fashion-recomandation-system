import cv2
import numpy as np

def detect_skin_tone(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    avg_color = np.mean(img, axis=(0, 1))

    if avg_color[0] > 200:
        return "Fair"
    elif avg_color[0] > 150:
        return "Medium"
    else:
        return "Dark"
