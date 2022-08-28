import time
import board
import busio
import digitalio
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_requests as requests
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from wifiConnect import wifiCon



# sends puts request
def buttomPutRequest(buttonNum, presetRequest):
    print(buttonNum + " pressed")
    response = requests.put(presetRequest)
    time.sleep(0.5)

# sends get requests
def buttonGetRequest(buttomNum, presetRequest):
    print(buttonNum + " pressed")
    response = requests.get(presetRequest)
    time.sleep(0.5)


def dehauReqs(presetNum):
    changedReq = "http://192.168.1.2:80/ISAPI/PTZCtrl/channels/1/presets/" + presetNum + "/goto"
    return changedReq

def hikReqs(presetNum):
    changedReq = "http://192.168.1.2:80/ISAPI/PTZCtrl/channels/1/presets/" + presetNum + "/goto"
    return changedReq
