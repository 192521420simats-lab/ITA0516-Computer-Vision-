
import cv2
import matplotlib.pyplot as plt

path = input("Enter the image path: ")
img = cv2.imread(path)

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    dilated = cv2.dilate(binary, kernel, iterations=1)

    plt.subplot(1, 3, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(binary, cmap="gray")
    plt.title("Binary Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(dilated, cmap="gray")
    plt.title("Dilated Image")
    plt.axis("off")

    plt.show()
