import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
plt.style.use('fivethirtyeight')
import statsmodels as sm
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics import tsaplots
from statsmodels.tsa.arima_model import ARIMA
import statistics

df = pd.read_excel("Daily/Egypt.xlsx",squeeze=True, parse_dates=True)
df = df[["Date", "LocalTransmission"]]
df.set_index("Date", inplace=True)
df.dropna(inplace=True)
##df['Date'] = pd.to_datetime(df['Date'])
df['LocalTransmission'] = df['LocalTransmission'].astype('int32')
#print (df.index)

diff1 = df.diff().fillna(df)
diff2 = diff1.diff().fillna(diff1)

##plt.plot(diff1)
##plt.title('diff1')
##plt.show()
##plt.plot(diff2)
##plt.title('diff2')
##plt.show()

tsaplots.plot_acf(diff2)
plt.title('ACF')
plt.show()

tsaplots.plot_pacf(diff2)
plt.title('PACF')
plt.show()
