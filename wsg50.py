import requests
import logging
import time
logger = logging.getLogger('gripper')
logger.setLevel(logging.DEBUG)

def convert(command):
    data = {
      '1207': command['width'],  # Target opening width of the fingers
      '1214': command['speed'], # Finger movement speed while positioning
      '1247': '0',  # Nominal width of the part to be gripped
      '1254': '100',  # Speed value used for closing the fingers
      '1261': '80',  # Force limit for gripping the part. If no force sensing fingers are installed, the force is approximated using the motor current.
      '1291': '88',  # Required clearance between the fingers when gripper is in open position
      '1298': '100',  # Speed value used for opening the fingers
      '1334': '2500', # Maximum acceleration when moving the gripper fingers.
      '1341': '50', # Maximum finger travel for clamping the part at the specified part width.
      '1348': '1', # The tolerance of the specified part width.
      'sender_id': '1221',
      'event_type': '0'
    }
    return data


def prePosition():

    logger = logging.getLogger('gripper')
    logger.info("Going to prePosition")
    print("Going to prePosition")
    command = {"width" : 110,
               "speed" : 100}
    execute(command)
    time.sleep(1)

def grip(width=30,speed=100):
    logger = logging.getLogger('gripper')
    logger.info("Going to grip")
    print("Going to grip")
    command = {"width" : width,
               "speed" : speed}
    execute(command)
    time.sleep(1)




def execute(data):
    gripperIP = "192.168.1.165"
    response = requests.post(f'http://{gripperIP}/motion.json', data=convert(data))


