
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = input("Enter the image path: ")
img = cv2.imread(path)

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    pts2 = np.float32([
        [50, 50],
        [cols - 50, 0],
        [0, rows - 50],
        [cols - 1, rows - 1]
    ])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.warpPerspective(img, matrix, (cols, rows))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("Perspective Transformation")
    plt.axis("off")

    plt.show()
