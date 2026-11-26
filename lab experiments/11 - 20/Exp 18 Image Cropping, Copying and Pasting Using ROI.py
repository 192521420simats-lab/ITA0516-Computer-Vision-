
import cv2
import matplotlib.pyplot as plt

path = input("Enter the image path: ")
img = cv2.imread(path)

if img is None:
    print("Image not found")
else:
    h, w = img.shape[:2]

    x = w // 4
    y = h // 4
    width = w // 2
    height = h // 2

    roi = img[y:y+height, x:x+width]

    copied = img.copy()
    copied[0:height, 0:width] = roi

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    plt.title("Cropped ROI")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(copied, cv2.COLOR_BGR2RGB))
    plt.title("Copied and Pasted")
    plt.axis("off")

    plt.show()
