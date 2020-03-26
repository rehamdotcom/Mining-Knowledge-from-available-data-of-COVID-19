import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import math
from statistics import mean

plt.style.use('fivethirtyeight')

df = pd.read_excel("Daily/Egypt.xlsx",squeeze=True, parse_dates=True)
df = df[["Date", "LocalTransmission"]]
df.set_index("Date", inplace=True)
df.dropna(inplace=True)
##df['Date'] = pd.to_datetime(df['Date'])
LocalTransmission = df['LocalTransmission'].astype('int32')
#print (df.head())
print (df.index)



result = ARMA(df, order=(2,1)).fit(disp=False)
print(result.summary())
#print(result.params)
predictions = result.predict(start="2020-03-01", end="2020-05-01")
#accuracy = result.score()
print (predictions)
##accuracy = result.score()
#print (accuracy)

result.plot_predict(start="2020-03-01", end="2020-05-01")
plt.suptitle('Prediction for postive cases in Egypt \n Algorithm used: ARMA', fontsize = 12)
plt.show()

##def mean_forecast_error(y, yhat):
##    return y.sub(yhat).mean()

def mean_forecast_error(LocalTransmission, predictions):
    return mean (sum(LocalTransmission, predictions))

mean_forecast_error(LocalTransmission, predictions)

print (mean_forecast_error)

