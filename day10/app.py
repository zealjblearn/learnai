import cv2
from pprint import pprint

pprint(cv2)
# image
img = cv2.imread("gpay.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap=cv2.VideoCapture(0)
print(cap)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Camera", frame)
    # if cv2.waitKey(0):
    #     break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

