import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

img_counter = 0  # Counter for saved images

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1) & 0xFF  # Check key press every frame

    # Capture image and exit window after saving
    if key == ord('c'):
        img_name = f"captured_image_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} saved!")
        img_counter += 1

        # Exit after saving
        break

    # Just close if 'q' is pressed
    if key == ord('q'):
        break

    # Also break if window is closed
    if cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
