import cv2 as cv
from filled_shape import filled_shape as fs
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--cam", "-c", dest='cam', default=False, action='store_true', help="Use cam as source")
parser.add_argument("--debug", default=False, action='store_false', help="show more contours and points")

arg = parser.parse_args()

if arg.cam:
    cap = cv.VideoCapture(0)
    last_time = time.time()
    while True:
        ret, frame = cap.read()
        if ret:
            
            text = f"FPS: {int(1 / (time.time() - last_time))}"
            last_time = time.time()
            cv.putText(frame, text, (10, 40), cv.FONT_HERSHEY_PLAIN, 0.8, (0, 255, 0), 2)

            fs.capture(frame, arg.debug)

        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break
    cap.release()
    cv.destroyAllWindows()
else:
    parser.parse_args(['--help'])
