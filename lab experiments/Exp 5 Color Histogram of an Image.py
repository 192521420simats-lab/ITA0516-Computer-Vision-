
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(path):
    img = cv2.imread(path)

    if img is None:
        print("Image not found. Check the path.")
        return

    colors = ["b", "g", "r"]
    labels = ["Blue", "Green", "Red"]

    for i in range(3):
        hist = cv2.calcHist(
            [img], [i], None, [256], [0, 256]
        )
        plt.plot(hist, color=colors[i], label=labels[i])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.show()

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

path = input("Enter the image path: ")
analyze_histogram(path)
