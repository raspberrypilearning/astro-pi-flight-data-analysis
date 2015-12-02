from matplotlib import pyplot
from csv import reader
from dateutil import parser

with open('../data/astro_pi_data_20150824_085954.csv', 'r') as f:
    data = list(reader(f))

temp = [i[3] for i in data[1::]]
time = [parser.parse(i[19]) for i in data[1::]]

pyplot.title('Temperature changes over Time')
pyplot.xlabel('Time/hours')
pyplot.ylabel('Temperature/$^\circ$C')

pyplot.plot_date(time, temp)
pyplot.show()
