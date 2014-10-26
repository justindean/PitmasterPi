#!/usr/bin/python


import smbus
import time
from time import sleep
import datetime
from subprocess import call
import sys
import xively
import dweepy
import requests

bus = smbus.SMBus(1)
FEED_ID = "xxxxxxxxxxx"
API_KEY = "xxxxxxxxxxx"
api = xively.XivelyAPIClient(API_KEY)
DWEET_KEY = 'xxxxxxxxx'
#I2C address
address = 0x4d
isHeating = True
P = 3
I = .05
B = 0

#xively function to return a datastream object.  If one exists it returns it, if not, it creates it.
def get_datastream(feed):
    try:
        datastream = feed.datastreams.get("BBQPitTemp")
        return datastream
    except:
        datastream = feed.datastreams.create("BBQPitTemp", tags="temperature")
        return datastream

def update_graphs_lite(current_temp):
     feed = api.feeds.get(FEED_ID)
     datastream = get_datastream(feed)
     datastream.max_value = None
     datastream.min_value = None
     datastream.current_value = current_temp
     datastream.at = datetime.datetime.utcnow()
     try:
         datastream.update()
     except requests.HTTPError as e:
         print "HTTPError({0}): {1}]".format(e.errno, e.strerror)

def update_dweet_logging(current_temp,target_temp):
    try:
        dweepy.dweet_for('XXXXXXX-DWEET-DEVICE-ID', {'key':DWEET_KEY,'pit_temp':current_temp,'target_temp':target_temp})
    except:
        pass 

def set_cooking_alert(target_temp): #Using Requests here until dweepy adds in alert/lock functionality
        alert_email = 'EMAIL-ADD%40EMAIL-DOMAIN.com'
        alert_url = 'https://dweet.io:443/alert/'+alert_email+'/when/[XXXXX-DWEET-DEVICE-ID]/if(dweet.pit_temp%20%3C%3D%20'+str(target_temp-30)+')%20return%20%22Too%20LOW%22%3B%20else%20if(dweet.pit_temp%20%3E%3D%20'+str(target_temp+30)+')%20return%20%22Too%20HIGH%22%3B?key='+DWEET_KEY
        print alert_url
        requests.get(alert_url)

def get_current_temp(): 
	data = bus.read_i2c_block_data(address, 1,2)
	val = (data[0] << 8) + data[1]
	return val/5.00*9.00/5.00+32.00

def get_current_temp_celcius(): 
        data = bus.read_i2c_block_data(address, 1,2)
        val = (data[0] << 8) + data[1]
        return val/5.00   
	
def turn_heat_on():
	print "Turning Fan On"
	call(["temp_relay_on", "hot"])
	
def turn_heat_off():
	print "Turning Fan Off"
	call(["temp_relay_off", "hot"])	
	
def PID_Control_Loop(target_temp):
    interror = 0
    heater_state = "off"
    cooking_temp_met = False
    print "Now entering PID Control Loop Function"   
    print target_temp
    previous_temp = int(get_current_temp())
    #Trying to prevent misreadings from groundloops from messing up temp swings
    while True:
        current_temp = int(get_current_temp())
        if current_temp > (109) and current_temp < (111):
            current_temp = previous_temp
        #Allowing for initial ramp up before setting the alerting
        if cooking_temp_met == False and current_temp >= target_temp:
            cooking_temp_met = True
            set_cooking_alert(target_temp)
            print 'setting up alert'    
        update_graphs_lite(current_temp)
        update_dweet_logging(current_temp,target_temp)
        print "You are in PID timer-while loop: Current Temp is %d and target temp is %d and INTERROR is %d" % (current_temp, target_temp, interror)
        error = (target_temp) - (current_temp)
        # Trying to prevent INTERROR from jumping too much when lid lifts, etc.  #autotune
        if error < 10 and error > 0:
            interror = interror + error
        power = B + ((P * error) + ((I * interror)))
        print "power is %d" % power
        previous_temp = current_temp
        for x in range(1,10):
            print x
            if (power > x**2): #May need tuning, still overshoots by power of 30, holds steady after that though
                if (heater_state=="off"):
                    heater_state = "on"
                    print "State = ON"
                    print current_temp
                    turn_heat_on()
                else:
                    print "Leaving the Heat ON"
            else:
                if (heater_state=="on"):
                    heater_state="off"
                    print "State is OFF"
                    turn_heat_off()
            sleep(1)        
        if (power < 10):
            sleep(10)        
        #if prev_power < power - 1000 OR prev_power > power + 1000: #lid must be off??            
            #sleep(180)

def main(argv):

	if len (sys.argv) < 2 :
		print "Usage: temperature_hold  [temperature] "
		sys.exit (1)	
	target_temp=sys.argv[1]
	try:
		target_temp=float(sys.argv[1])
	except ValueError:
		print "the argument is not a number"
		sys.exit (1)
	print "target temp =" , target_temp
        PID_Control_Loop(target_temp)


if __name__ == "__main__":
	main(sys.argv[1:])
