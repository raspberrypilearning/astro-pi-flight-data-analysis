# Graphing CSV data with matplotlib

## Loading the csv data.

Python is capable of handling csv data using the **csv module**.

1. Create a new Python file  and call it `temperature.py`.

1. First you'll need to import the `reader` function from the `csv` module.

	```python
	from csv import reader
	```

1. Next you can open the csv sheet and store the data in a list.

	```python
	with open('filename.csv', 'r') as f:
		data = list(reader(f))
	```

1. Replace `filename.csv` with the name of the file you are using - `astro_pi_data_20150824_085954.csv` for instance.

1. Run the file and then switch over to the interpreter, and you can have a look at the contents of the `data` list that you have created. This will show you the headers of the csv sheet.

```python
data[0]
```

1. If you want to have a look at the first set of values in the data, then you can use:

```python
data[1]
```

1. You can see the last items in the list, by typing:

```python
data[-1]
```

## Getting specific data sets.

At the moment the values are stored as a *list of lists*. To graph the data, you'll want specific data sets. For instance, you might want to get the temperature.

Looking at the headers of the csv sheet, there is a choice of temperature measurements to choose from.

```
'ROW_ID', 'temp_cpu', 'temp_h', 'temp_p', 'humidity', 'pressure', 'pitch', 'roll', 'yaw', 'mag_x', 'mag_y', 'mag_z', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'reset', 'time_stamp'
```

`temp_p`, which is the temperature recorded by the pressure sensor, is probably the best one to use. This is the *3rd* item in the list, as lists are indexed from `0`.

1. You can use a *list comprehension* to extract the temperatures from the *list of lists*. This line of code, takes the **third** value from **every** item in data.

	```python
	temp = [i[3] for i in data]
	```

1. You can look at the contents of some of the temp data, by typing into the interpreter. This will show you the start of the list, which is the header:

	```python
	temp[0]
	```

1. This will show you the first 10 items in the list:

	```python
	temp[0:10]
	```

1. You don't actually want the header, so you can alter the *list comprehension* so that the first item of the `data` list is ignored.

	```python
	temp = [i[3] for i in data[1::]]
	```

1. You can do the same again, to get the date-time stamps from `data`.

	```python
	time = [i[19] for i in data[1::]]
	```

## Your first graph

The **Matplotlib** module (along with *numpy* and *scipy*) is one of the reasons so many mathematicians and scientists use Python. It's an excellent way of drawing graphs.

1. You'll need to import the module, to begin with:

```python
from matplotlib import pyplot
```

1. You need only two lines to graph your data:

```python
pyplot.plot(range(len(temp)), temp)
pyplot.show()
```

1. `pyplot.plot()` needs to be given two *iterables*. In the above, you have given it `range(len(temp))` which is all numbers from `0` up to the length of the `temp` list. You've also given it `temp` which is the set of temperatures. `pyploy.show()` draws the graph. Save and run your file.

## Adding dates and times

At the moment, the date-time isn't being used in the graph. The reason you cant really use it at the moment is because the data is not in a format that matplotlib can recognise

```python
'2015-08-20 23:58:30'
```

This string needs changing to a **datetime** object, which is fortunately quite easy.

1. You need to import the **parser** function from the **dateutil** module to begin with.

	```python
	from dateutil import parser
	```

1. To convert a date in *string* format, to a *datetime* object, the syntax is fairly simple. For instance:

	```python
	parser.parse('2015-08-20 23:58:30')
	```

1. You want to convert each date that is added to the `time` list, so you can edit your list comprehension to read:

	```python
	time = [parser.parse(i[19]) for i in data[1::]]
	```

1. Now you can change your `pyplot.plot()` call so it looks like this

	```python
	pyplot.plot(time, temp)
	pyplot.show()
	```

1. Your complete code should look like:

	```python
	from matplotlib import pyplot, dates
	from csv import reader
	from dateutil import parser

	with open('../data/astro_pi_data_20150824_085954.csv', 'r') as f:
		data = list(reader(f))

	temp = [i[3] for i in data[1::]]
	time = [parser.parse(i[19]) for i in data[1::]]

	pyplot.plot(time, temp)
	pyplot.show()
	```

## Adding Titles and Axis

Graphs should always be titles and have labelled axis. Again, this is trivial with matplotlib.

1. First you can add a title:

	```python
	pyplot.title('Temperature changes over Time')
	```

1. Then the *x axis*:

	```python
	pyplot.xlabel('Time/hours')
	```

1. And lastly the *y axis*:

	```python
	pyplot.ylabel('Temperature/$^\circ$C')
	```

[< Back to the worksheet](worksheet.md#how-do-i-analyse-the-data)
