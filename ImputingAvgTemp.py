from sklearn.impute import KNNImputer
import pandas as pd

data = pd.read_excel("Countries.xlsx")
data = data[['Latitude', 'AvgTemp']]

#print(data.head())

imputer = KNNImputer(n_neighbors=9)
data_filled = imputer.fit_transform(data)

print (data_filled)
