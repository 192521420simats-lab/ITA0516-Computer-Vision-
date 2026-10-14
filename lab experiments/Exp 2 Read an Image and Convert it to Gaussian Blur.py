
import cv2
import matplotlib.pyplot as plt

path = input("Enter the image path: ")
img = cv2.imread(path)

if img is None:
    print("Image not found. Check the path.")
else:
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
    plt.title("Gaussian Blur")
    plt.axis("off")

    plt.show()
