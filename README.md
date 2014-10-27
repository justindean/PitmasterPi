PitmasterPi
===========

BBQ Automated Temperature Controller using Raspberry Pi and some Devops type practices/toolchains for improving the state of "PitOps".

The goal of this project is to marry the Devops type philosophies, spirit and practices with the art of making great BBQ in order to produce a much more consistant and quality finished product each and every time.  Obviously its a very loose coupling of the two worlds, but there are definitely efficiencies to be gained by leveraging the practices the Devops community has been continuing to develop and tune.  

![](https://github.com/justindean/PitmasterPi/blob/master/Images/Ribs-Done.JPG)

The Problem:
===========

We've all been there before.  You've invited a bunch of people over for dinner.  You've bought your meat and ingredients.  You have a lot of things to do that day, sons football game, trip to the store, pickup daughter from the mall, mow the lawn and most of all you need to get the house nice and cleaned up ready for guests.  The issue is you need to get the BBQ pit fired up early, so you can get it dialed into the right temperature.  Then you have to get your meat on there and get the pit temperature leveled back out to the right temps once again.  Once the meats on the grill, you start your all day job of tending the fire.  Every 15 minutes you need to make sure its stable at the desired temp, a full day of messing with air vents and dealing with hot and cold spells on the pit.  You can't just take off and do the things you need to today, you are officially on PitOps.  Your significant other now has to pick up the slack on everthing else or you risk the chances of burnt BBQ if you try to slip off for more than a few minutes.  That's a bad start to the day for everyone.  Even after you have dedicated the day to manually babysitting the pit, you still have most likely had temperature drops and spikes along the way that definitely has an impact on the food quality.  Let's say it was the best BBQ you have ever produced, could you do it again exactly the same?  How long did it cook?  What temperatures? Will you remember the details in a month?  I think we can agree, we need better PitOps.

PitOps:
===========

By (loosely) leveraging the DEVOPS "CAMS" principals we can add much more efficiency, automation and ultimately change the culture around BBQ in every household.  

## Culture:  

Starting with culture.  The process of BBQ is very labor entensive and manual.  It is very high touch throughout the whole process and everyone's turns out different.  Its viewed as a very artistic process where the pitmaster puts his heart and soul into the process to produce a peice of meat with his very essence in it.  This sounds a lot like the same artisan Ops/Devs who roll thier code into production on beautifully hand crafted servers that have been chiseled to perfection right there on the spot in live production.  One of a kind, artisan servers with the essence of each individual engineer who touched it last, while may sound romantic on the surface we all know is a terrible idea.  I think we can change the BBQ culture to see the craft and artistry of the process should be focused on the meat itself, ingredients, spice rubs, marindates, (Source Code if you will) and NOT the cooking pipeline itself.  The cooking process is ripe for productionalizing.

## Automation: 

This is where the main bang for our buck is.  Automating the BBQ cooking process to make it much more efficient, predictable, repeatable and ultimately to change the game when it comes to PitOps (no more babysitting the bbq pit).

### -Open Source and Revision Control
First and foremost, all of the code is open source and lives on github.  This gives you 100% access and control to know exactly how the algorithm/process works and allows for easy tweeks, changes and feature additions.  Most BBQ controllers out there are completely proprietary with no access to the inter workings.  

### -Repeatable Code Deployment
Given Raspberry Pi's are a hobby board you may wish to use it for other tasks besides BBQ.  Go for it.  When you need it to cook again, just deploy the lastest version from github. (will be adding cleaner packaging/template/install in the future).  This also allows you to keep multiple PitmasterPi's identical in case you have multiple BBQ pits or if you are on a competition BBQ team where having identical systems is more critical.

### -Starting the Fire:  
Starting the fire used to be a pretty big process (pain).  You had to get a fire going or light your charcoal, then after 30 minutes when it start to ash over you close up the BBQ pit and hope (pray) that the pit will even out somewhere remotely close to your desired cook temp.  Usually it would overshoot by a ton and you have to play with air vents for an hour to get it dialed in.  The process of lighting the fire is still a bit manual unfortunately (for now) but has been greatly reduced down to less than 1 minute.  Since we have automated fire control, now we can use a MAPP gas torch, torch one small section of the firebasket for 30 seconds to get a cherry red spot going then close up the pit and "deploy".  PitmasterPi will take care of the rest.

![](https://github.com/justindean/PitmasterPi/blob/master/Images/fire-start.JPG)

### -Initial Temperature Ramp:  
When you start PitmasterPi, you give it your desired cooking temp setpoint.  It will then ramp up the temperature to the set point by stoking the fire in a very controlled manner.  It uses a PID algorithm combined with some sensible delays based on proximity to your setpoint to ramp up the temperature without ending up with a raging fire and overshooting the set point.  Once its up to temp it will send you a message and you can put the meat on.

##### BBQ Pit Starting to ramp up to temps.  (Definitely need a nice case to house all the electronics)
![](https://github.com/justindean/PitmasterPi/blob/master/Images/pit_ramping3.jpg)

### -Cooking Temperature Hold:  
This is the main function of PitmasterPi.  Its main goal in life is to keep the fire stoked to the appropriate level to keep the cooking chamber dialed into your desired set temp.  All day, all night.  This is the piece that takes PitOps from being like working in the NOC on Cyber Monday after a major press release to more like being Secondary On-call for a very stable system.  PitmasterPi uses the same PID algorithm to dynamically keep temps dialed in within a couple degrees.  Having this functionality has changed BBQ'ing from being a huge "Waterfall" type production with lots of prep, scheduling and logistics to manage "BBQ Release Day" to a much more "Continual Delivery" model where I have an automated PitOps pipeline in place, where I can confidently deploy a large piece of meat into production and know it will produce consistent results.

### -Efficiency:
You can already see the massive efficiency gains on the operational side of things, but there is also a huge efficiency gain on the resource side as well.  By having very tight control of the fire, we save a massive amount of fuel.  In my pit for example, I can get ~20 hours from a 10lb bag of charcoal cooking at 220*F.  That's double what I would get in a manual setup.  PitmasterPi will save you hard earned OPEX dollars!

## Metrics:

What fun would an automated BBQ Pit be without metrics.  This is an area where you may wish to expand into your own favorite tools of choice.  While I wanted to initially use the toolset from work Tcollector/OpenTSDB, Splunk, etc, I thought it would be much more IoT friendly and approachable to use simple cloud based tools easily accessible by everyone.

### -Temperature Timeseries Graphing and Trending:  
For logging temperature data for real-time and historical trending we use Xively.  Theres a nice xively python module to allow PitmasterPi to send timeseries temp data every few seconds.  

##### Xively Dash showing a nice 6hr view of steady pit temps:
![](https://github.com/justindean/PitmasterPi/blob/master/Images/xively_6hr.png)


##### Xively Snapshot from Iphone at kids football game:
![Xively Snapshot from Iphone - 6hr view](https://github.com/justindean/PitmasterPi/blob/master/Images/xively-iphone-6hr.PNG)

### -Temperature Datastore:  
PitmasterPi also uses Dweet.io for storing temperature data.  Dweet.io allows for ridiculously simple messaging (and alerting) for devices.  It's like twitter for devices and is gaining traction in the Internet of Things community.  The dweet.io key/value datastore data we send can be leveraged for multiple purposes (dashboards, alerting, etc).

### -Real-Time Dashboard: 
We use Freeboard.io.  Freeboard.io is a very simple dashboard creater that uses the message data we put into dweet.io.  Gives us a nice dashboard for real time BBQ Pit data on any browser.  I.e. Sitting at your sons football game, you can watch your Pit temps on your iphone.

#### Freeboard.io Real-Time Dashboard:
![Freeboard.io real-time dashboard](https://github.com/justindean/PitmasterPi/blob/master/Images/freeboard.png)


#### Freeboard.io Real-Time Dashboard snaptop from Iphone while at kids football game:
![Freeboard.io real-time dashboard snapshop from Iphone while at kids football game](https://github.com/justindean/PitmasterPi/blob/master/Images/freeboard-iphone.PNG)


### -Monitoring/Alerting: 
This is one area where we can expand quite a bit.  For the moment, PitmasterPi is using dweet.io as the alerting platform.  Once the pit is done ramping up to temperature and enters the cooking stage, it will automatically setup a monitor/alert in dweet.io that will trigger an alert if the pit gets too high or too low.  It will send you emails/text, so you can go about your day without constantly watching the pit thermometer.  This is critical for those all-nighter Briskets and Pork Butts.  No more getting up 5 times a night to check on it, just go to sleep and PitmasterPi will take care of tending the fire and if something crazy happens you'll get a text message.

## Sharing:

Just as sharing is important and critical for success for any shop, team or company, sharing is imporant around PitmasterPi and PitOps.  There are so many devices, tools and practices out there that are constantly evolving that every project can be constantly improved by the shared knowledge and contributions of others.  In the spirit of sharing, I will be putting all the code, hardware and build information in this repo for others to use and hopefully contribute to.  There are a lot of things left to build (food temps, PID algorithm autotuning, servos?, cheaper hw alternatives, lid off detection, etc).

PitmasterPi Hardware:
======

-Raspberry Pi (currently using model B+), 5v power supply

-Raspbian OS

-USB Wireless dongle

-12v Squirrel cage style blower fan

-Adjustable output 12v power supply (i set mine to 6v which gets the right amount of power/airflow from blower fan)

-High temperature K type Thermocouple with Stainless sheeth tip (made for oven or bbq ideally)

-Thermocouple connector and amplifier: http://www.robogaia.com/raspberry-temperature-controller-plate.html (I use this, I'll explain more below)

-Relay Board for switching power:  http://www.robogaia.com/raspberry-temperature-controller-plate.html (same as above)

-Case: Need a case to house all the components nicely. TBD

#### Raspberry Pi with Temperature Control Board - Notice the 2 relays
![Raspberry Pi with Temperature Control Board - Notice the 2 relays](https://github.com/justindean/PitmasterPi/blob/master/Images/rpi.JPG)


#### Thermocouple attached to cooking chamber
![Thermocouple attached to cooking chamber](https://github.com/justindean/PitmasterPi/blob/master/Images/thermocouple.JPG)


#### Blower attached to bottom area of firebox
![Blower attached to bottom area of firebox](https://github.com/justindean/PitmasterPi/blob/master/Images/blower.JPG)


PitmasterPi Operations Basics:
=====

The basic principal of the PitmasterPi is that it controls the temperature of the cooking chamber of the BBQ Pit by controlling the temperature of the fire in the fire box.  It controls the fire by controlling the amount of air/oxygen allowed to be consumed by the fire.  Oxygen is a main component for combustion, so more oxygen more fire more heat and less oxygen less fire and less heat.  It sounds kind of lofty to think we could control something as wild and untamable as fire, but in practice it works quite well.  

We start with a good BBQ pit.  You need to be able to seal up the firebox area to where the only source of air is the PitmasterPi blower.  This is crucial to keeping steady/predictable temps.  If there are air gaps in your firebox (doors, etc) a nice breeze could stoke your fire out of control.

1. Connect Thermocouple into cooking chamber of your pit
2. Connect Blower fan to firebox (3/4" black pipe couplings work great, JBweld to blower, mount/seal a pipe nipple at bottom of your firbox)
3. Turn on PitmasterPi, wifi connected and ssh'able, plug in dc wall adapter to supply power to fan
4. Load firebasket with charcoal/wood chunks
5. Torch middle section for 30 seconds to get baseball sized cherry red area started
6. Seal up firebox and pit, keep exhaust vent open for proper (outbound) airflow
7. SSH to PitmasterPi, start a screen session, initialize the relays (sudo ./temperature_controller_init)
8. Start your BBQ Process and supply it your desired set temp (sudo ./PitmasterPi.py 225) 
9. PitmasterPi will then control the blower fan to stoke the fire to ramp it to the Set temp. 
10. Put on meat
11. Once at temp, PitmasterPi will setup alerting and constantly tend to the fire while trying not to overshoot the temp (PID)
12. You can monitor temps along the way via the python process itself has a lot of verbose output, xively portal graphs, dweet.io data feeds, freeboard.io dashboard or you can go old school and look at the thermometer mounted on your pit.


PitmasterPi Todo List:
=====

While the basic operations of pit tending works well and really makes PitOps much easier, there are a TON of things on the radar to make it much better:

-Multipe Temperature Probes - Temperature Probes for the Meat.  This seems obvious, but its much tricker since we are using High Temp thermocouples which are analog instead of the much easier digital sensors.  Since we are dealing with fire and high temps, the digital sensors would fry, so as such we need to be able to collect analog data from the sensor, convert it to a unit of measure we can use (C or F).  Since the voltage measurements are so low with analog thermocouples we need to have circuitry to amplify the signal for accurate readings as well as to offset the temperature changes at the cold junctions of the board itself.  This is where the Robogaia temperature controller board comes into play.  It provides everything needed to connect an analog K type thermocouple to the raspberry pi to get temp measurements AND it also combines 2 relays to allow us to switch power to something (in our case its the blower fan).  In order to add more thermocouples to the raspberry pi, we would need another board (cost prohibitive) and/or find a sleeker alternative for adding multiple analog thermocouples to the RPi.  In its current state, this probably means building the circuit board yourself, soldering, etc, which makes it much less user friendly for the general population.

-Better case.  Need to put it all together nicely so its not just laying on the ground.

-PID algorithm auto learning and tuning.  Everyones pit is different, would be great to use some machine learning/robotics techniques to auto learn the thermal properties of the pit and tune the P, I and D values accordingly.

-Cook and Hold.  Once we get food probes going, we can add in the ability to ramp temps, hold them for the cook, when food temps are almost done then ramp down the pit temp to match the food done temp and hold it there for you until its time to eat.

-Bi-directional controls.  When it sends you an alert it would be nice if you could give it a command of some sort.

-Raspberry Pi failure detection.  Need to build in methods to keep an eye on the raspberry pi itself and be able to gracefully handle a crash.

-Lid open detection.  When you open the lid to put on the meat or baste it, etc, the pit temp drops.  This causes the PitmasterPi to start stoking the fire way beyond whasts needed.  When the lid goes back on, you may overshoot the set temp for a while as it stoked it too much.  


Recent PitmasterPi Cooks:
======

### 16 Hour Pork Butt for Pulled Pork Sandwiches:
![](https://github.com/justindean/PitmasterPi/blob/master/Images/pork-butt-pit.JPG)

![](https://github.com/justindean/PitmasterPi/blob/master/Images/pork-butt.JPG)

![](https://github.com/justindean/PitmasterPi/blob/master/Images/pulled-pork.JPG)

### Smoked Sausage:
![](https://github.com/justindean/PitmasterPi/blob/master/Images/sausages2.jpg)

### St. Louis Style Ribs:
![](https://github.com/justindean/PitmasterPi/blob/master/Images/ribs-uncooked.JPG)

![](https://github.com/justindean/PitmasterPi/blob/master/Images/ribs-done-smoking.JPG)


