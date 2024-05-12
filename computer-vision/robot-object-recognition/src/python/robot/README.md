# Robot

## Project set-up

### YOLOv3

```
cd Desktop
cp yolo_v3/yolov3.cfg artificial-intelligence/computer-vision/robot-object-recognition/src/python/robot
cp yolo_v3/yolov3.weights artificial-intelligence/computer-vision/robot-object-recognition/src/python/robot
```

### Virtual environment

#### Create

Navigate to this directory:
```
cd artificial-intelligence/computer-vision/robot-object-recognition/src/python/robot/
```

Create virtual environment for Mac OS:

```
virtualenv robot-venv
```

#### Activate

Activate virtual environment for Mac OS:

```
source ./robot-venv/bin/activate
```

### Install packages

```
sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev libopenblas-dev
```

```
pip install "picamera[array]"
```

```
pip install opencv-python
```

```
pip install numpy
```

### Run the code

```
python main.py
```