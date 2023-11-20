#!/bin/sh
git clone https://github.com/ultralytics/ultralytics
cd ultralytics

# Setup Coral dependencies
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt update
sudo apt install libedgetpu1-std -y
sudo apt install python3-pycoral -y
pip install -r requirements.txt