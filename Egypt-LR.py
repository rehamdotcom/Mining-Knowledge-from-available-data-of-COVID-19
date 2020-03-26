from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_excel ('WeatherAndPositiveCases/Daily/Egypt.xlsx')
df = df[['Delta', 'LocalTransmission']]
df.dropna(inplace=True)

#df['Date'] = pd.to_datetime(df['Date'])

x = df['Delta'].astype('int32')
y = df['LocalTransmission'].astype('int32')

def fit_line(x,y):

    slope = (((mean(x) * mean(y)) - mean(x*y))/
            ((mean(x)*mean(x)) - mean(x*x)))

    intercept = mean(y) - slope*mean(x)
    
    return slope,intercept

def squared_error(yactual, ypredicted):
    return sum ((ypredicted-yactual)**2)

def coefficientofdetermination(yactual,ypredicted):
    y_mean_line = [mean(yactual) for y in yactual]
    squared_error_regr = squared_error(yactual, ypredicted)
    squared_error_y_mean = squared_error(yactual, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)

slope, intercept = fit_line(x,y)

regression_line = [(slope*x)+intercept for x in x]

predict_x = np.arange(start=63, stop=100, dtype=np.int32)
predict_y = (slope*predict_x)+intercept
r_squared = coefficientofdetermination(y, regression_line) * 100

print('predictions for number of positive cases in Egypt' , predict_y, sep='\n')
print('Accuracy = ', r_squared, '% (Cofficient of determination is R-squared)')

plt.suptitle('Prediction for postive cases in Egypt')
plt.title('Algorithm used: Linear Regression')
plt.xlabel('Years')
plt.plot(x, y, label='Actual (feature)')
plt.plot(predict_x, predict_y, label='Predicted (label)')
plt.legend()
plt.ylabel('Number of tourists')
plt.scatter(x,y)
plt.scatter(predict_x, predict_y)
plt.plot(x, regression_line, color='b')
plt.show()


