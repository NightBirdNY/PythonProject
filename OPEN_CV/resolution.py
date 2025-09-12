#changin resolution of live vidoe
import cv2 as cv
import time

# Kamerayı başlat
capture = cv.VideoCapture(0)

# MJPEG formatını zorla
capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))

# Çözünürlük ayarla (kamera destekliyor olmalı)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 360)

# FPS hesaplama için başlangıç ayarları
frame_count = 0
start_time = time.time()
fps = 0  # <--- başlangıçta fps tanımlanmalı

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    frame_count += 1
    elapsed = time.time() - start_time

    if elapsed >= 1.0:
        fps = frame_count / elapsed
        frame_count = 0
        start_time = time.time()

    # FPS değeri görüntüye yazılsın
    cv.putText(frame, f'FPS: {fps:.2f}', (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv.imshow("Live Video", frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
