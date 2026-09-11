import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, blanco_negro = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow('Blanco & Negro', blanco_negro)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows