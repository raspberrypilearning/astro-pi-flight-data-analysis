## Astro Pi Flight Data Analysis

![](images/columbus.jpg)

If you have completed the [Sense HAT data logger](https://projects.raspberrypi.org/en/projects/sense-hat-data-logger/) project you will finish with a large Comma Seperated Value (CSV) file, ready to be looked at.

Alternatively you might have completed the [Astro Pi Mission Space Lab](https://astro-pi.org/mission-space-lab/guidelines/life-in-space) challenge and have a CSV to analyse once your data has been returned from the International Space Station.

## What's in a CSV files?

A CSV file contains lines of data seperated by commas. Usually there is also a header row in a CSV file as well, which describes the data. CSV files are an excellent way of storing tables of data, but they can be hard for humans to read through.

Here is an example of two lines from a CSV file, with the header row and the first line of data.

```
Date/Time,Latitude,Longitude,Temperature,Humidity,Pressure,Compass,MagX,MagY,MagZ,Pitch,Roll,Yaw,AccelX,AccelY,AccelZ,R,G,B,C,Motion
2022-01-31 12:21:15,6.833,152.032,32.7,57.5,1013.6,117,-5.4,-10.6,-4.4,0,360,117,0,0,0,29,27,24,84,1
```

Here's the same data but in a table, making it a little easier to read.
```
|Date/Time|Latitude|Longitude|Temperature|Humidity|Pressure|Compass|MagX|MagY|MagZ|Pitch|Roll|Yaw|AccelX|AccelY|AccelZ|R|G|B|C|Motion|

|2022-01-31 12:21:15|6.833|152.032|32.7|57.5|1013.6|117|-5.4|-10.6|-4.4|0|360|117|0|0|0|29|27|24|84|1|
```


sensor measurements in rows and columns. The columns each represent a different type of sensor, with an extra column to record a timestamp. Each *row* gives you a reading for every sensor, with the timestamp showing when the readings were taken. You can use this to look at how the sensor readings are changing over time.

Here is an example:

ROW_ID|SENSOR 1|SENSOR 2|SENSOR 3|SENSOR 4|...|TIME STAMP
---|---|---|---|---|---|---
1|35.29|26.86|26.03|60.43|...|01/01/2015 23:58:50
2|35.31|26.86|26.02|60.46|...|01/01/2015 23:59:00
3|35.2|26.87|26.02|60.45|...|01/01/2015 23:59:10

So all measurements on a single row were taken at the time shown in the timestamp; note that they are each ten seconds apart. The CSV file you'll get from orbit thankfully won't have Sensor 1, 2 or 3, but more intuitive names that describe the data.

Here is a list of the columns you'll have:

Column name|Meaning|Source
---|---|---
ROW_ID|A unique identifying number for each row. If you're collaborating with other people, it may be useful to have a way to specify the exact row number when you find something interesting in the data.|Database auto-increment.
temp_cpu|The temperature of the Raspberry Pi B+ CPU in degrees *Celsius*.|Raspberry Pi GPU mailbox (`/sys/class/thermal/thermal_zone0/temp`).
temp_h|The temperature in degrees *Celsius*.|Sense HAT humidity sensor.
temp_p|The temperature in degrees *Celsius*.|Sense HAT pressure sensor.
humidity|The *percent* relative humidity.|Sense HAT humidity sensor.
pressure|Air pressure in *millibars*.|Sense HAT pressure sensor.
pitch|An angle between 0 and 360 *degrees* giving the current pitch orientation.|Calculated from combined Sense HAT accel, gyro and mag readings. 
roll|An angle between 0 and 360 *degrees* giving the current roll orientation.|Calculated from combined Sense HAT accel, gyro and mag readings.
yaw|An angle between 0 and 360 *degrees* giving the current yaw orientation.|Calculated from combined Sense HAT accel, gyro and mag readings.
mag_x|The magnetic field strength of the X axis in *microteslas* (µT).|Sense HAT magnetometer.
mag_y|The magnetic field strength of the Y axis in *microteslas* (µT).|Sense HAT magnetometer.
mag_z|The magnetic field strength of the Z axis in *microteslas* (µT).|Sense HAT magnetometer.
accel_x|The acceleration intensity of the X axis in *Gs*.|Sense HAT accelerometer.
accel_y|The acceleration intensity of the Y axis in *Gs*.|Sense HAT accelerometer.
accel_z|The acceleration intensity of the Z axis in *Gs*.|Sense HAT accelerometer.
gyro_x|The rotational intensity of the X axis in *radians per second*.|Sense HAT gyroscope.
gyro_y|The rotational intensity of the Y axis in *radians per second*.|Sense HAT gyroscope.
gyro_z|The rotational intensity of the Z axis in *radians per second*.|Sense HAT gyroscope.
reset|A copy of the Raspberry Pi CPU reset register. This is useful for looking at the frequency and effect of single event upsets. The values are only recorded once per boot.|Raspberry Pi GPU mailbox (`vcgencmd get_rsts`).
time_stamp|The time at which the sensors were measured and the row was created.|Astro Pi real-time clock.

There is an excellent guide to help you understand the sensors [here](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) if you need to familiarise yourself.


## Where can I get the CSV files?

Right here! There are three CSV files on offer; the first two were collected in the Columbus module and the third one is from the Node 2/Unity module. Look [here](http://www.esa.int/Our_Activities/Human_Spaceflight/International_Space_Station/Building_the_International_Space_Station3) if you need a map of the ISS modules.

Unit|Location on ISS|Length|Download
---|---|---|---
Astro Pi Vis (Ed)|Columbus|2 weeks|[Download](https://github.com/raspberrypilearning/astro-pi-flight-data-analysis/raw/master/data/Columbus_Ed_astro_pi_datalog.csv.zip)
Astro Pi Vis (Ed)|Columbus|4 weeks|[Download](https://github.com/raspberrypilearning/astro-pi-flight-data-analysis/raw/master/data/Columbus2_Ed_astro_pi_datalog.csv.zip)
Astro Pi IR (Izzy)|Node 2|2 weeks|[Download](https://github.com/raspberrypilearning/astro-pi-flight-data-analysis/raw/master/data/Node2_Izzy_astro_pi_datalog.csv.zip)

If you need help loading the file, we suggest searching the internet for help specifically related to the spreadsheet software you're using.

There's also an example CSV file, recorded using an Astro Pi on the ground. This was just left on an office desk to collect the data, but it could be useful for comparison. You can download it [here](https://github.com/raspberrypilearning/astro-pi-flight-data-analysis/raw/master/data/astro_pi_data_20150824_085954.zip).

