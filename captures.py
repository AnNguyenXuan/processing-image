import cv2
import RPi.GPIO as GPIO
import time
def main():
    BT1 = 21
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global namewindow
    namewindow = "Camera User"
    capture = cv2.VideoCapture (0) # khởi động camera
    print("Capture đã ok") 
    while True: # nếu camera được mở
        ret, frame = capture.read() # đọc video từ camera 
# frame được trả về là dạng ma trận; numpy.aray print(type(frame)) 
# chiều dài và chiều rộng là cỡ của ma trận; print(frame.shape)
        if GPIO.input (BT1) == GPIO.LOW:
            while True:
            # Hiện ảnh ra màm hình từ biến frame
            # cv2.imshow sẽ đọc frame, chuyển frame ra dạng hình ảnh 
                cv2.imshow("Ảnh chụp camera", frame) 
                cv2.waitKey() 
                cv2.destroyWindow("Ảnh chụp camera")
                break


try:
    main ()
except KeyboardInterrupt:
    GPIO.cleanup ()
    cv2.destroyWindow (namewindow)

