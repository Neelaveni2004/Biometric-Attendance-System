import cv2
import csv
from datetime import datetime

cap = cv2.VideoCapture(0)
attendance_marked = False

with open("attendance.csv", "a", newline="") as file:
    writer = csv.writer(file)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Biometric Attendance System", frame)

        key = cv2.waitKey(1)

        if key == ord('a') and not attendance_marked:
            name = "Student"
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            writer.writerow([name, date, time])
            attendance_marked = True
            print("Attendance Marked")

        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
      
