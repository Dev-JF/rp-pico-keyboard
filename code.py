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


pins = [GP0, GP1]

def buttonAssign(gp):
    digitalio.DigitalInOut(board.gp)


# camera address
CAM_ONE_IP = "http://192.168.1.4"
# CAM_ONE_IP = "192.168.1.4"
CAM_TWO_IP = "192.168.1.2"

wifiCon()


def buttomPutRequest(buttonNum, presetRequest):

    try:
         print(buttonNum + " pressed")
         response = requests.put(presetRequest)
         time.sleep(0.5)
    except:
        print(buttonNum + " unreachable try again")


presetTwoDehau = "http://192.168.1.2:80/ISAPI/PTZCtrl/channels/1/presets/3/goto"

button1 = buttonAssign(pins[1])
button1.switch_to_input(pull=digitalio.Pull.UP)

button2 = buttonAssign(pins[2])
button1.switch_to_input(pull=digitalio.Pull.UP)

# when the assigned button is pressed, run its set code
while True:
    if button1.value == False:
        try:
         print("bttn1 pressed")
         response = requests.put("http://192.168.1.2:80/ISAPI/PTZCtrl/channels/1/presets/3/goto")
         time.sleep(0.5)
        except:
            print("Preset 1 unreachable try again")


    if button2.value == False:

        buttomPutRequest("button 2", presetTwoDehau)

