# RaspiSecurity
Home Surveillance with Raspberry with only ~100 lines of Python Code.
For technical details check the realted [medium post](https://hackernoon.com/raspberrypi-home-surveillance-with-only-150-lines-of-python-code-2701bd0373c9). Hope you like it.

# Installation to a new Raspberry2 B+

## Install necessary libraries 
- ```sudo apt-get update```
- ```sudo apt-get install build-essential python2.7-dev python-setuptools```
- ```sudo su```
- ```sh install_opencv.sh``` 
- ```sudo easy_install pip```
- ```sudo pip install picamera```

## Setup config files
- Copy conf.json.sample to conf.json
- Set sender email address, email server credentials, and destination email address(es) to email alerts

## Run the agent
- ```python server.py ```
- Go to given URL on the terminal
- Activate or deactivate the agent. The idea here, if you are close to your house, your phone will connect to your net before you enter the house, 
then you can deactivate the agent to prevent wrong alert on you. You should also activate it before leaving the house. It will give you some time to 
leave the house then become active. 




