import cv2

#url = 'http://192.168.0.125:8080/video'
cap = cv2.VideoCapture(0)

# Read the first three frames
frame1 = cap.read(1)
frame2 = cap.read(1)
frame3 = cap.read(1)

# Convert frames to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)

def img_diff(x, y, z):
    d1 = cv2.absdiff(x, y)
    d2 = cv2.absdiff(y, z)
    # Perform a bitwise 'and' operation on the difference images
    final_img = cv2.bitwise_and(d1, d2)
    return final_img

while True:
    ret, frame = cap.read()
    if not ret:
        break

    motion = img_diff(gray1, gray2, gray3)

    # Update the previous frames
    gray1 = gray2
    gray2 = gray3
    gray3 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('LIVE', frame)
    cv2.imshow("motion", motion)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
