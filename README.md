### Mining-Knowledge-from-available-data-of-COVID-19

##### In this repository, I experiment which of the features is positively correlated with the outbreak of COVID-19 throughout the world. Features include data of inbound tourism across each of the affected countries, georgraphical subfeatures such 'land area', 'population', 'population density', 'latitude' and 'longtitude' accross each of the affected countries, and other climatic subfeatures such as 'Average Temperature', 'Relative Humidity' and 'Average Daylight Hours' also accross each of the affected countries.

##### I aimed for gathering data from multiple sources, situation reports from World Health Organization (WHO), from United Nations (UN) data and others. 

##### Sciket learn libraries were used for both imputing missing values* and for computing the correlation.

#### Hightlights on the experiment on March 23rd, 2020 are as following:

##### . The correlation results show highest positive correlation between total observed positive cases and population across each of the affected countries.

##### . The correlation results show highest second positive correlation between total observed positive cases and inbound tourism across each of the affected countries.

##### . Correlation results show no significant correlation between climatic conditions with either the total observed positive cases nor the observed slope of increase/decrease accross each of the affected countries.

![Image of Yaktocat](https://github.com/rehamdotcom/Mining-Knowledge-from-available-data-of-COVID-19/blob/master/corr.png?raw=true)

----------------------------------------------------------
##### * Imputation using KNN were applied for predicting missing values for average daylight hours and average temperature accross each of the affected countries using latitude feature and non-missing values for average daylight hours and average temperatures. Imputed average daylight hours have a mean error of 0.5 hours more or less. Imputed average temperature is also not precise as I only use here the latitude feature whereas the degree of elevation feature (which is highly correlated with average temperatures) is not available at this time.
