
import cv2
import matplotlib.pyplot as plt

path = input("Enter the image path: ")
img = cv2.imread(path)

if img is None:
    print("Image not found. Check the path.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("Equalized Image")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title("Original Histogram")

    plt.subplot(2, 2, 4)
    plt.hist(equalized.ravel(), 256, [0, 256])
    plt.title("Equalized Histogram")

    plt.tight_layout()
    plt.show()
