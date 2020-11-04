import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas_datareader as pdr
from pandas_datareader import data
from datetime import datetime
import csv
import talib 

def main():

	with open('05-07-2017-TO-04-07-2018SBINEQN.csv', 'r') as f:
    		sarray= list(csv.reader(f, delimiter=','))
	'''readcsv('04-07-2016-TO-03-07-2018SBINALLN.csv')'''
	'''export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH '''
	sarray=np.array(sarray)
	date=sarray[1:,2].tolist()
	date = [dt.datetime.strptime(dat, '"%d-%m-%Y"').date() for dat in date]
	close= sarray[1:,8]
	date=np.array(date)
	close=np.array(close,dtype=np.float)
	date = matplotlib.dates.date2num(date)
	plt.plot_date(dates, values)
	output = talib.SMA(close)
	momentum = talib.MOM(close, timeperiod=5)
	macd, macdsignal, macdhist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
	plt.clf()
	plt.plot(date, macd)
	plt.plot(date,macdsignal)
	plt.plot(date,macdhist)
	plt.xlabel('Date')
	plt.savefig('macd.pdf', format='pdf')
if __name__ == '__main__':
    main()
