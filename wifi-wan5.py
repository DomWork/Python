# wifi-wan?.py
# This program runs for 240 hours (28800 lots of 30 seconds) and checks that
# the computer has an IP address (i.e. is successfully connected to the router by wifi)
# every 30 seconds. It prints the time and OK if all is good into a spreadsheet lan-wan-log.csv
# It also prints to screen. It keeps a note of how many times the wifi connection went down.
# wifi7 onwards - once there has been a wifi down, an LED on pin 11 blinks, so no need to even look at code or spreadsheet
# It checks on the WAN / internet as well to see if there is a connection to the outside world.
# For ease, it logs to a separate file when the wi-fi or wan are down, but not when they are fine: lan-wan-erros.csv
# From wifi-wan3 onwards, there are now 3 LEDs that flash to signal status. So can just look at LEDs to know status.
# Ctrl-C ends the program at any time.

#Import the libraries used # this could do with being tidied up
import urllib
import urllib.request
import requests
import time
from time import sleep, strftime, time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # Pin 11 is a red LED that flashes the number of times wifi goes down 
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # Pin 16 is a yellow LED that is constantly on while WAN is down
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Pin 18 is a green LED that very briefly flashes every loop to let you
                                            # know the program is running and has not crashed
from subprocess import check_output

#Set up some variables initial values
flag=0 #counts number of times wifi goes down 
down=0 # toggle for wifi down
wan=0 #toggle for internet down
wanCount=0 #counts number of times WAN / internet is down

#Function to write an entry to spreadsheet 7 columns wide - to write the log file for every loop
def write_wifi(status):
    with open("/home/pi/lan-wan-log.csv", "a") as log:
        log.write("{0},{1},{2},{3},{4},{5},{6}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(status)," Wi-fi down ",str(flag)," WAN down ",str(wanCount)," times"))

#Function to write an entry to spreadsheet 7 columns wide - to only write to an error file if there is an error
def write_error(status):
    with open("/home/pi/lan-wan-errors.csv", "a") as log:
        log.write("{0},{1},{2},{3},{4},{5},{6}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(status)," Wi-fi down ",str(flag)," WAN down ",str(wanCount)," times"))

#Function to blink the LED if the wifi connection goes down, and blink the number of times it has gone down
def blink_led(flag):
    if flag!=0:
        loop=range(flag)
        for j in loop:
            GPIO.output(11, GPIO.HIGH) # Turn on RED LED
            sleep(0.3) # Sleep for 1 second
            GPIO.output(11, GPIO.LOW) # Turn off
            sleep(0.2) # Sleep for 1 second

#Function to blink the LED to show the program is still running and has not crashed
def blink_working():
            GPIO.output(18, GPIO.HIGH) # Turn on GREEN LED
            sleep(0.03) # Sleep for 1 second
            GPIO.output(18, GPIO.LOW) # Turn off
            sleep(0.07) # Sleep for 1 second
            GPIO.output(18, GPIO.HIGH) # Turn on - two very quick flashes are just a little more noticable than one
            sleep(0.03) # Sleep for 1 second
            GPIO.output(18, GPIO.LOW) # Turn off

#Function to test the internet connection /WAN
#It would be better to do two additional things here:
#1 Improve it by having a library of different web sites and randomly use them, rather than just one all the time
#2 Improve it by checking a second web site if the first one fails, before flagging an internet failure
def wan_on():
    global wan
    global wanCount
    while True:
        try:
            requests.get('https://grantadesign.com').status_code #status code is 200 when successful, a load of errors if not
#            requests.get('https://www.goo--gle.com/').status_code #Uncomment this line to simulate WAN going down 
#                                                                   for testing purposes - swap this line for one above
            wan=0
            #Internet is ok
            return(wan, wanCount)
        except:
            #Internet is down
            if wan==0:
                wan=1
            else:
                wan=2
            if wan==1:
                wanCount+=1
            return(wan, wanCount)

#Here is the Main loop of the program - START - First Line
#Could neaten this code up by pulling the wifi-checking part out into a function
try: # This try loop goes forever? Unless Ctrl-C is pressed?
    for i in range (28800):
        blink_working()
        wifi_ip = check_output(['hostname', '-I'])
        howlong = len(wifi_ip) #if there is a connection the string showing the IP address is 15 characters long
#        howlong=1  #Uncomment this line to simulate wi-fi going down for testing purposes  
        if howlong == 15:
            status = "All OK"
            wan_on() #Only if the wifi is ok is it worth checking the WAN, so that is why it is tested here
            if wan>=1:
                status = "Internet DOWN!!!"
                write_error(status)
            write_wifi(status)
            print (strftime("%H:%M:%S"),str(status),"   Wi-Fi down ",str(flag)," WAN down ",str(wanCount)," times") #print a short message to screen
            down=0
        else:
            status = "Wi-Fi DOWN!!!"
            write_wifi(status)
            write_error(status)
            print (strftime("%Y-%m-%d %H:%M:%S"),str(status),"   Wi-Fi down ",str(flag)," WAN down ",str(wanCount)," times") #print a longer message to screen - easily noticable
            if down==0:
                down=1 #this is used to increment the flag that lists the number of times it is down
            else:
                down=2 #this prevents the flag incrementing each time through the loop if it is during the same down-period
        if down==1:
            flag+=1 #flag of number of times the internet has gone down only increases each time there is an error, not each time it runs through the loop
        blink_led(flag)
        if wan!=0: #Simply leave WAN-down LED on permanently while it is down, don't bother flashing.
            GPIO.output(16, GPIO.HIGH) # Turn on LED and leave on while WAN is down
        else:
            GPIO.output(16, GPIO.LOW) # Turn off LED while WAN is OK
        sleep(30) # this controls the time between test iterations

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this program
    print ("End")




