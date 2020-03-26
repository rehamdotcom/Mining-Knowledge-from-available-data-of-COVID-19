from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import svm

df = pd.read_excel ('../00Daily/Australia.xlsx')
df.dropna(inplace=True)

#df['Date'] = pd.to_datetime(df['Date'])

X = df.loc[:,'Delta']
y = df.loc[:,'LocalTransmission']

#print(df.tail(1))

test = np.arange(start=57, stop=100, dtype=np.int32)
#test = test.reshape(1,-1)
#print (test)
#print (test.shape)

clf = svm.SVR(kernel='linear', C = 1.0)
#clf = svm.SVR(kernel='poly', C = 1.0, degree=4)
#clf = svm.SVR(kernel='rbf', C = 1.0, gamma=0.01)

clf.fit(X[:,None],y)

accuracy = clf.score(X[:,None],y)
prediction = clf.predict(X[:,None])
#print(prediction)
print("Predictions on May 1st, 2020 are " , clf.predict([[100]]), " postive cases")
print ("Accuracy = ", accuracy * 100 , "%")

plt.plot(X,y)
plt.plot(X, prediction)
plt.suptitle('Prediction for postive cases in Australia \n Algorithm used: SVR-Linear Kernel', fontsize = 12)
plt.show()
