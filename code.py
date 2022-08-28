import time
import board
import busio
import digitalio
from digitalio import DigitalInOut
# will need to remove/ replace with pico w libs once it is moved over
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
from camRequest import buttomPutRequest
from camRequest import buttomGettRequest
from camRequest import dehauReqs
from camRequest import hikReqs



# camera address - may no need this with function dehauReqs and hikReqs function
CAM_ONE_IP = "http://192.168.1.4"
# CAM_ONE_IP = "192.168.1.4"
CAM_TWO_IP = "192.168.1.2"

# calls the function in the wifiConnect file
wifiCon()

# Assigns the button to the gpio pin - make this another file?
button1 = digitalio.DigitalInOut(board.GP0)
button1.switch_to_input(pull=digitalio.Pull.UP)

button2 = digitalio.DigitalInOut(board.GP1)
button2.switch_to_input(pull=digitalio.Pull.UP)




# when the assigned button is pressed, run its set code
while True:
    if button1.value == False:

        presetReq = dehauReqs("3")
        buttomPutRequest("button1", presetReq)

    if button2.value == False:
        presetReq = dehauReqs("2")
        buttomPutRequest("button 2", presetReq)

