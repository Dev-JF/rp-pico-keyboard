# rp-pico-keyboard


This application uses micrpython libraries and airlift libraries (for the wifi module)


Current config:

I am currently refactoring the code to be more efficient and less cluttered. I am also updating the code to work for the pico w
This means that the arduino airlift libs are no longer required.


Overview:

Connects to wifi and sends http request to ip cameras when a button is pressed.


Add your wifi details to the secrets file


In the camRequest file

to change the request information either change dehauReqs or hikReqs to string to a request you want to be sent, if there is multiple variants use string concatination so you can easily allow for slight adjustments for each variaton of request. note if you change function names dont forget to change them in the code file when importing them.

e.g.

def dehauReqs(presetNum):
    changedReq = "http://192.168.1.2:80/ISAPI/PTZCtrl/channels/1/presets/" + presetNum + "/goto"
    return changedReq
    
can be come:


def dehauReqs(ipAdd, presetNum):
    changedReq = "http://" + ipAdd + "/ISAPI/PTZCtrl/channels/1/presets/" + presetNum + "/goto"
    return changedReq
    
this goes for the get and put requests in the same file if you wish to change what is printed, what is  sent as a request, etc.


in the main file named code.py:

wifiCon calls the function from the wifiConnect file and initalises the wifi - this may be changed when migrating to the pico w


Assign the right buttons to the right gpio pins and then add the new button to the while loop
