import cv2
import copy
import RPi.GPIO as GPIO 
def nothing (x):
    pass
def main():
    BT1 = 21
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (BT1, GPIO.IN, pull_up_down=GPIO. PUD_UP) 
    cap= cv2.VideoCapture (0)
    print ("Cap ok")
    while True:
        if GPIO.input (BT1) == GPIO.LOW:
            print("Press BT1")
            cv2.namedWindow('image')
            # thạo các thanh slider để chỉnh ngưỡng màu
            cv2.createTrackbar ('lowH', 'image', 0, 180, nothing) 
            cv2.createTrackbar ('highH', 'image', 179, 180, nothing)
            cv2.createTrackbar ('lows', 'image', 0, 255, nothing)
            cv2.createTrackbar ('highs', 'image', 255, 255, nothing)
            cv2.createTrackbar ('lowV', 'image', 0, 255, nothing)
            cv2.createTrackbar ('highV', 'image', 255, 255, nothing)
            GPIO.setmode (GPIO. BCM)
            GPIO.setup (BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            while True:
                _, src = cap.read()
                # đặt vị trí trên slider
                ilowH = cv2.getTrackbarPos ('lowH', 'image') 
                ihighH = cv2.getTrackbarPos ('highH', 'image')
                ilows = cv2.getTrackbarPos ('lows', 'image')
                ihighs = cv2.getTrackbarPos ('highs', 'image')
                ilowV = cv2.getTrackbarPos ('lowV', 'image')
                ihighV= cv2.getTrackbarPos ('highV', 'image') 
                hsv = cv2.cvtColor (src, cv2.COLOR_BGR2HSV) # chuyển sang không gian HSV
                # Phân ngưỡng trong không gian HSV 
                mask= cv2.inRange (hsv, (ilowH, ilows, ilowV), (ihighH, ihighs, ihighV))
                # sử dụng mask để lọc màu với ảnh gốc 
                result = cv2.bitwise_or (src, src, mask=mask)
                cv2.imshow('image', result)
                # Press q to exit
                if cv2.waitKey (1) & 0xFF== ord('q'):
                    GPIO.cleanup()
                    break
try:
    main ()
except KeyboardInterrupt:
    GPIO.cleanup() 
    cv2.destroyAllWindows ()
