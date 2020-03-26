import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('countries.xlsx')
df = df[['Total Postive Cases', 'Slope of PC increase (local cases)','FirstLocalCaseDelta','InboundTourists (Predicted)', 'landAreafilled', 'Population', 'pop.densityfilled', 'Latitude', 'Longtitude', 'AvgTempNullsImputed', 'RelativeHumidity (%)', 'AvgSunshineNullsImputed']]
df.dropna(inplace=True)
x = df[['Slope of PC increase (local cases)','FirstLocalCaseDelta','InboundTourists (Predicted)']]
pd.set_option('display.max_columns', None)
correlation_table = df.corr()

print (correlation_table.head())

plt.matshow(correlation_table)
plt.show()
