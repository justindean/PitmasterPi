PitmasterPi
===========

BBQ Automated Temperature Controller using Raspberry Pi and PitOPS Practices

The goal of this project is to marry the Devops philosophies, spirit and practices with the art of making great BBQ in order to produce a much more consistant and quality finished product each and every time.  

The Problem:
===========

We've all been there before.  You've invited a bunch of people over for dinner.  You've bought your meat and ingredients.  You have a lot of things to do that day, sons football game, trip to the store, pickup daughter from the mall, mow the lawn and most of all you need to get the house nice and cleaned up ready for guests.  The issue is you need to get the BBQ pit fired up early, so you can get it dialed into the right temperature.  Then you have to get your meat on there and get the pit temperature leveled back out to the right temps once again.  Once the meats on the grill, you start your all day job of tending the fire.  Every 15 minutes you need to make sure its stable at the desired temp, a full day of messing with air vents and dealing with hot and cold spells on the pit.  You can't just take off and do the things you need to today, you are officially on PitOps.  Your significant other now has to pick up the slack on everthing else or you risk the chances of burnt BBQ if you try to slip off for more than a few minutes.  That's a bad start to the day for everyone.  You need better PitOps.

PitOps:
===========

By (loosely) leveraging DEVOPS "CAMS" principals we can add much more efficiency, automation and ultimately change the culture around BBQ in every household.  

Culture:  
=====
Starting with culture.  The process of BBQ is very labor entensive and manual.  It is very high touch throughout the whole process and everyone's turns out different.  Its viewed as a very artistic process where the pitmaster puts his heart and soul into the process to produce a peice of meat with his very essence in it.  This sounds a lot like the same artisan Ops/Devs who roll thier code into production on beautifully hand crafted servers that have been chiseled to perfection right there on the spot in live production.  One of a kind, artisan servers with the essence of each individual engineer who touched it last, while may sound romantic on the surface we all know is a terrible idea.  I think we can change the BBQ culture to see the craft and artistry of the process should be focused on the meat itself, ingredients, spice rubs, marindates, (Source Code if you will) and NOT the cooking pipeline itself.  The cooking process is ripe for productionalizing.

Automation: 
=====
This is where the main bang for our buck is.  Automating the BBQ cooking process to make it much more efficient, predictable, repeatable and ultimately to change the game when it comes to PitOps (no more babysitting the bbq pit).

-Starting the Fire:  Starting the fire used to be a pretty big process (pain).  You had to get a fire going or light your charcoal, then after 30 minutes when it start to ash over you close up the BBQ pit and hope (pray) that the pit will even out somewhere remotely close to your desired cook temp.  Usually it would overshoot by a ton and you have to play with air vents for an hour to get it dialed in.  The process of lighting the fire is still a bit manual unfortunately (for now) but has been greatly reduced down to less than 1 minute.  Since we have automated fire control, now we can use a MAPP gas torch, torch one small section of the firebasket for 30 seconds to get a cherry red spot going then close up the pit and "deploy".  PitmasterPi will take care of the rest.

-Initial Temperature Ramp:  When you start PitmasterPi, you give it your desired cooking temp setpoint.  It will then ramp up the temperature to the set point by stoking the fire in a very controlled manner.  It uses a PID algorithm combined with some sensible delays based on proximity to your setpoint to ramp up the temperature without ending up with a raging fire and overshooting the set point.  Once its up to temp it will send you a message and you can put the meat on.

-Cooking Temperature Hold:  This is the main function of PitmasterPi.  Its main goal in life is to keep the fire stoked to the appropriate level to keep the cooking chamber dialed into your desired set temp.  All day, all night.  This is the piece that takes PitOps from being like working in the NOC on Cyber Monday after a major press release to more like being Secondary On-call for a very stable system.  PitmasterPi uses the same PID algorithm to keep temps dialed in within a couple degrees.

Metrics:
===
What fun would an automated BBQ Pit be without metrics.  This is an area where you may wish to expand into your own favorite tools of choice.  While I wanted to initially use the toolset from work Tcollector/OpenTSDB, Splunk, etc, I thought it would be much more IoT friendly and approachable to use simple cloud based tools.

-Temperature Timeseries Graphing and Trending:  For logging temperature data for real-time and historical trending we use Xively.  Theres a nice xively python module to allow PitmasterPi to send timeseries temp data every few seconds.  

-Temperature Datastore:  PitmasterPi also uses Dweet.io for storing temperature data.  Dweet.io allows for ridiculously simple messaging (and alerting) for devices.  It's like twitter for devices and is gaining traction in the Internet of Things community.  The dweet.io key/value datastore data we send can be leveraged for multiple purposes (dashboards, alerting, etc).

-Real-Time Dashboard: We use Freeboard.io.  Freeboard.io is a very simple dashboard creater that uses the message data we put into dweet.io.  Gives us a nice dashboard for real time BBQ Pit data on any browser.  I.e. Sitting at your sons football game, you can watch your Pit temps on your iphone.

-Monitoring/Alerting: This is one area where we can expand quite a bit.  For the moment, PitmasterPi is using dweet.io as the alerting platform.  Once the pit is done ramping up to temperature and enters the cooking stage, it will automatically setup a monitor/alert in dweet.io that will trigger an alert if the pit gets too high or too low.  It will send you emails/text, so you can go about your day without constantly watching the pit thermometer.  This is critical for those all-nighter Briskets and Pork Butts.  No more getting up 5 times a night to check on it, just go to sleep and PitmasterPi will take care of tending the fire and if something crazy happens you'll get a text message.

Sharing:
===
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

PitmasterPi Operations Basics:
=====


