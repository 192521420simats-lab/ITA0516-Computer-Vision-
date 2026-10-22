
import cv2
import matplotlib.pyplot as plt

path = input("Enter the image path: ")
img = cv2.imread(path)

if img is None:
    print("Image not found")
else:
    h, w = img.shape[:2]

    bigger = cv2.resize(img, (w * 2, h * 2))
    smaller = cv2.resize(img, (w // 2, h // 2))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB))
    plt.title("Bigger")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
    plt.title("Smaller")
    plt.axis("off")

    plt.show()
