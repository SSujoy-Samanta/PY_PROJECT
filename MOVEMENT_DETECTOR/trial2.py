import cv2
import telepot
import time
token='6799766729:AAGhqM-MGhwJ9XbLqcDaFBrGtmkNWKeP-dw'
recever_id='5106410815'

# Set the URL of the video stream
url = 'http://192.168.0.110:8080/video'

# Create a VideoCapture object to read the video stream
cap = cv2.VideoCapture(url)

# Initialize the previous frames
gray1 = None
gray2 = None
gray3 = None

# Define a function to perform frame differencing
def img_diff(x, y, z):
  d1 = cv2.absdiff(x, y)
  d2 = cv2.absdiff(y, z)
  final_img = cv2.bitwise_and(d1, d2)
  return final_img

# Start the video loop
while True:
  # Read a frame from the video stream
  ret, frame = cap.read()

  # If the frame is not empty, process it
  if ret:

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # If the previous frames are not initialized, initialize them
    if gray1 is None:
      gray1 = gray
      gray2 = gray
      gray3 = gray

    # Compute the difference between the current frame and the previous two frames
    motion = img_diff(gray1, gray2, gray3)

    # Update the previous frames
    gray1 = gray2
    gray2 = gray3
    gray3 = gray

    # Display the current frame and the motion image
    cv2.imshow('LIVE', frame)
    cv2.imshow('motion', motion)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    if(motion is not None):
      t = time.localtime()
      cur_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
      bot=telepot.Bot(token)
      bot.sendMessage(recever_id,f"!!! MOTION IS DITECTED AT {cur_time}>>>>")


# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
