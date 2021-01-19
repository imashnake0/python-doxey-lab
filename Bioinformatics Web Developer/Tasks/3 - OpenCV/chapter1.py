import cv2 as xcv

# Read images, videos, and webcams?

### IMAGES ###
'''
img = xcv.imread("./google-earth-view-6545.jpg")

xcv.imshow("Bruh", img)
xcv.waitKey(0)
'''

### VIDEOS ###
'''
cap = xcv.VideoCapture("mat.webm")

while True:
    success, img = cap.read()
    xcv.imshow("Bruh_1", img)
    
    # what does waitKey(1) do? 0xFF == 111111 and ord('x') == decimal('x').
    if xcv.waitKey(1) & 0xFF == ord('x'):
        break
'''

### WEBCAM ###
'''
cap = xcv.VideoCapture(0)

# sets brightness?
cap.set(10, 1) 

while True:
    success, img = cap.read()
    xcv.imshow("Bruh_2", img)
    if xcv.waitKey(1) & 0xFF == ord('x'):
        break
'''