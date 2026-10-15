
import cv2
import time

path = input("Enter the video path: ")
cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Video not found")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 25

    print("Press N for normal, S for slow, F for fast, Q to quit")

    mode = "normal"

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        delay = int(1000 / fps)

        if mode == "slow":
            delay *= 3
        elif mode == "fast":
            delay = max(1, delay // 3)

        key = cv2.waitKey(delay) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('s'):
            mode = "slow"
        elif key == ord('f'):
            mode = "fast"
        elif key == ord('n'):
            mode = "normal"

    cap.release()
    cv2.destroyAllWindows()
