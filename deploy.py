######################################################################
# Maintained and developed by the Electric-Go-Kart team at CSU
# Last modified 11/16/2023
# This file is the main file for the deployment of the APDde project
# It is run on the Raspberry Pi 4
######################################################################

# 1. Start TCP stream with this command: libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888
# 2. Run this file with the command: python3 deploy.py

import os
from ultralytics import YOLO
import cv2

def start_tcp_stream():
    os.system("libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888")

def stop_tcp_stream():
    os.system("killall libcamera-vid")

def main():
    # Run the TCP stream
    model = YOLO(f"models/{model}.pt")
    start_tcp_stream()
    # Run the YOLO model
    results = model('tcp://127.0.0.1:8888', stream=True)
    # if 'q' is pressed, stop the TCP stream
    while True:
        for result in results:
            boxes = result.boxes
            probs = result.probs
        if cv2.waitKey(1) == ord('q'):
            break
    stop_tcp_stream()

if __name__ == "__main__":
    main()