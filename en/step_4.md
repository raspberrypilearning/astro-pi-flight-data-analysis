## What to look for

There are a many patterns and anomolies that you could look for, when trying to discover interesting events that might affect the lives of astronauts on the ISS. One such event that might be of interest is the ISS re-boost

The ISS is always losing 50 to 100 metres of altitude per day, and if left unchecked it would eventually re-enter the atmosphere and burn up like a meteorite! This happens because the ISS is in low Earth orbit (LEO), and even at an altitude of 400 km there is still a tiny amount of atmosphere present. That air creates drag on the ISS, which causes its orbit to slowly decay over time.

To avoid it burning up on re-entry the ISS is given a re-boost by a docked spacecraft. A reboost fires the thrusters for a while to increase the altitude by the desired amount.

![](images/reboost_firing.jpg)

The graph below shows time on the horizontal axis, and the altitude of the ISS in kilometres on the vertical. You can see that, every now and again, the altitude jumps back up. These are the reboosts and you can see they happen in a somewhat irregular way.

![](images/ISS_altitude.png)

The Astro Pi cannot measure altitude from inside the ISS, so this is not part of the CSV data. However, when an ISS reboost occurs the Pi can detect the force of **acceleration** being applied by the spacecraft thrusters. In microgravity, the accelerometer X, Y and Z axes should always read close to zero Gs. However, at least one or two axes will detect some force when the thrusters are being fired.

The crew say that they can feel when a reboost is happening, so the Sense HAT [accelerometer](https://github.com/raspberrypilearning/astro-pi-guide/blob/master/sensors/movement.md) should definitely detect it. Therefore, you should be able to work out when the ISS reboosts occurred and how long they lasted. Go [here](http://www.heavens-above.com/IssHeight.aspx) for the latest altitude graph; you may be able to correlate this with the data in the CSV files.

**If you are entering the Astro Pi challenge, you need to be aware that you only have a three hour time period in which your experiment will run, and the date and time that your experiment will start can not be predicted. This should factor into what data you choose to collect.**
