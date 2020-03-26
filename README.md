### Mining-Knowledge-from-available-data-of-COVID-19

##### In this repository, I experiment which of the features is mostly positively correlated with the outbreak of COVID-19 throughout the world. Features include data of 'inbound tourism'* across each of the affected countries, georgraphical subfeatures such 'land area', 'population', 'population density', 'latitude' and 'longtitude' accross each of the affected countries, and other climatic subfeatures such as 'Average Temperature', 'Relative Humidity' and 'Average Daylight Hours' also accross each of the affected countries.

##### I aimed for gathering data from multiple sources, situation reports from World Health Organization (WHO), from United Nations (UN) data and others. 

##### Sciket learn libraries were used for both imputing missing values**, for computing the correlation and for carrying out the forecast using SVR model. Whereas StatsModels libraries were used for carrying out the rest of the forecasts.

#### Hightlights on the experiment on March 21st, 2020 are as following:

##### . The correlation results show highest positive correlation between total observed positive cases and population across each of the affected countries.

##### . The correlation results show highest second positive correlation between total observed positive cases and inbound tourism across each of the affected countries.

##### . Correlation results show no significant correlation between climatic conditions with either the total observed positive cases nor the observed slope of increase/decrease accross each of the affected countries.

![Image of Yaktocat](https://github.com/rehamdotcom/Mining-Knowledge-from-available-data-of-COVID-19/blob/master/corr.png?raw=true)

#### Forecast for positive cases for each of the affected countries are exeucted using different models as following: 
##### . Simple Linear Regression Model (LR) 
##### . Auto Regression Model (AR) 
##### . Moving Average Model (MA) 
##### . Auto Regression Moving Average Model (ARMA) 
##### . Auto Regression Integrated Moving Average Model (ARIMA) 
##### . Suppor Vector Regression Model (Linear, Poly and RFB kernels) (SVR) 
##### . Simple Exponential Smoothing Model (SES) 
##### . Holt Winters Exponential Smoothing Model (HWES) 


----------------------------------------------------------
##### * Data is only available for the timeframe between 2010 thru 2018 where 2019 is not out yet. Estimates of 2019 are a pure prediction based on the existing history data using a linear regression equation.


##### ** Imputation using KNN were applied for predicting missing values for average daylight hours and average temperature accross each of the affected countries using latitude feature and non-missing values for average daylight hours and average temperatures. Imputed average daylight hours have a mean error of 0.5 hours more or less. Imputed average temperature is also not precise as I only use here the latitude feature whereas the degree of elevation feature (which is highly correlated with average temperatures) is not available at this time.
