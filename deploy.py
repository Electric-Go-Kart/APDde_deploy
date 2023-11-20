######################################################################
# Maintained and developed by the Electric-Go-Kart team at CSU
# Last modified 11/16/2023
# This file is the main file for the deployment of the APDde project
# It is run on the Raspberry Pi 4
######################################################################
# #!/bin/sh

# # Setup APD_deploy folder
# git clone https://github.com/ultralytics/yolov5
# cd yolov5
# git checkout 79bca2bf64da04e7e1e74a132eb54171f41638cc
# cd ..
# mv detect.py ./yolov5/
# mv 528Project/ ./yolov5/
# mv run_it.sh ./yolov5/
# cd yolov5
# mkdir runs

# # Setup Coral dependencies
# echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
# curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
# sudo apt update
# sudo apt install libedgetpu1-std -y
# sudo apt install python3-pycoral -y
# pip install -r requirements.txt
# pip install numpy --upgrade
# # Import statements
import os

if __name__ == '__main__':
    