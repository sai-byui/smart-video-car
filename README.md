## Sunfounder Smart Video Car Kit for Raspberry Pi

Quick Links:

 * [About this kit](#about_this_kit)
 * [Update](#update)
 * [Trouble Shootings](#trouble)
    * [I2C Trouble](#i2c_trouble)
    * [_tkinter.TclError](#tkinter.tclerror)

<a id="about_this_kit"></a>
### About this kit:
"The SunFounder Smart Video Car Kit for Raspberry Pi is composed of Raspberry Pi, DC-DC Step-down Voltage Module, USB camera, DC motor driver, and PCA9685-based Servo Controller. From the perspective of software, the smart car is of client/server (C/S) structure. The TCP server program is run on Raspberry Pi for direct control of the car. And the video data are acquired and delivered via the open source software MGPJ-streamer in a real-time manner. The TCP client program is run on PC to send the control command. Both the client and server programs are developed in Python language. The smart car is developed based on the open-source hardware Raspberry Pi and integrates the knowledge of mechanics, electronics, and computer, thus having profound educational significance." /[1/]

#### Notice:
Before you run the client routine, you must first run the server routine.

<a id="update"></a>
### Update:

<a id="trouble"></a>
### Trouble Shootings:
<a id="i2c_trouble"></a>
#### I2C Trouble

	IOError: [Errno 2] No such file or directory
	
	Error accessing 0x40: Check your I2C address
	
	IOError: [Errno 5] Input/output error

This normally means Raspberry Pi could not find the I2C device. So here's what you can do:
 - **Hardware problem**:<br>
 	If you are using a DC adapter for your Raspberry Pi, you need to connect the GND between Servo Controller and Raspberry Pi. Because they are common-grounded by the micro USB, and if you use a DC adapter, you have to make another wire for common-ground.
 - **Software problem**:<br>
 	Just Run the i2cHelper.py with

 		sudo python i2cHelper.py
 	And after `i2cdetect`, and you should see your Servo Controller's address: 0x48

<a id="tkinter.tclerror"></a>
#### _tkinter.TclError

    pi@raspberrypi:~/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/client $ sudo python cali_client.py
    Traceback (most recent call last):
      File "cali_client.py", line 7, in <module>
        top = Tk()   # Create a top window
      File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1813, in __init__
        self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
    _tkinter.TclError: no display name and no $DISPLAY environment variable

 This usually happens when you try to run `cali_client.py` or `client_App.py` on Raspberry Pi remotely. Like using PuTTy.
  - Reason:
    `cali_client.py` and `client_App.py` run under the `tkinter`, which need a $DISPLAY, usually a GUI. Remotely log in to Raspberry Pi normally under bash, which is a CLI.
  - Solution:
    Try run the `cali_client.py` and `client_App.py` directly on your PC or Mac. It needs Python 2.7 installed on your computer. So:
    1. Go to python.org, download the lastest release of Python 2.7 for the operating system you are using, and install.
    2. Go to [the github repository](https://github.com/sunfounder/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi), and download the source code by clicking the green button on the right.
    3. Unzip the zip file.
    4. Edit the `HOST` in `cali_client.py` or `client_App.py` with Python IDLE (in Windows, usually, right click the .py file and select "Edit in IDLE"), and select **Run** => **Run Module   F5** to run the module.

----------------------------------------------
\[1\]	SunFounder, Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi.
