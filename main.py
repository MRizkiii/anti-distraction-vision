import cv2

kamera = cv2.VideoCapture(0)

print(kamera)

while True:
    ret, frame = kamera.read()
    cv2.imshow("CCTV", frame)

# Cek apakah lo nekan tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release() # Lepas bookingan kamera
cv2.destroyAllWindows() # Tutup semua jendela video