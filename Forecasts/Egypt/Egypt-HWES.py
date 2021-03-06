import statsmodels.api as sm
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import math
from statistics import mean

plt.style.use('fivethirtyeight')

df = pd.read_excel("../00Daily/Egypt.xlsx",squeeze=True, parse_dates=True)
df = df[["Date", "LocalTransmission"]]
df.set_index("Date", inplace=True)
df.dropna(inplace=True)
##df['Date'] = pd.to_datetime(df['Date'])
LocalTransmission = df['LocalTransmission'].astype('int32')
#print (df.head())
print (df.index)



result = ExponentialSmoothing(df).fit()
print(result.summary())
#print(result.params)
predictions = result.predict(start="2020-02-15", end="2020-05-01")
#accuracy = result.score()
print ("Predictions: " ,predictions, sep='\n')
##accuracy = result.score()
#print (accuracy)

#result.plot_predict(start="2020-03-01", end="2020-05-01")
plt.plot(predictions)
plt.suptitle('Prediction for postive cases in Egypt \n Algorithm used: HWES', fontsize = 12)

plt.show()

##def mean_forecast_error(y, yhat):
##    return y.sub(yhat).mean()

def mean_forecast_error(LocalTransmission, predictions):
    return mean (sum(LocalTransmission, predictions))

mean_forecast_error(LocalTransmission, predictions)

print (mean_forecast_error)

##res.plot_predict(start="2020-03-01", end="2020-04-01")
##plt.show()

##fig, ax = plt.subplots()
##ax = df.loc['2020-03-01':].plot(ax=ax)
##fig = res.plot_predict('2020-02-25', '2020-04-01', dynamic=True, ax=ax, plot_insample=False)
##plt.show()

##res.predict(start="2020-03-01", end="2020-04-01")
##predict = res.predict(len(df), len(df))
##print(predict)
##plt.plot(predict)
##plt.show()
