# **read url:**
data=pd.read_csv("/home/cusp/el2666/Applied_Data_Science/data_hw_3_4.csv")
data.head()

# **move data:**
os.system("mv data.csv " + os.getenv("PUIDATA"))

import from CUSP Data Facility:
import os 
import pandas as pd
DFDATA = os.getenv("DFDATA")
%pylab inline
DFDATA
DFDATA = "/gws/open/NYCOpenData/nycopendata/data/"
df_gas = pd.read_csv(DFDATA + "/uedp-fegm/1414245967/uedp-fegm")
df_gas.columns

loading json:
import pylab as pl
import json
import urllib.request as ulr
%pylab inline
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=" + \
"NewYork&mode=Json&units=metric&cnt=7&APPID="+os.getenv("OPENWEATHKEY") 
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

more about json plotting and accessing:
https://github.com/fedhere/PUI2016_fb55/blob/master/Lab2_fb55/APIreadingJson.py.ipynb

#download, move data to $PUIDATA, and read data in 
!curl -O https://data.cityofnewyork.us/api/views/rgfe-8y2z/rows.csv
cmd = "mv rows.csv " + os.getenv("PUIDATA")

unzip:
!curl -O http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/mn_mappluto_16v1.zip
os.system("unzip mn_mappluto_16v1.zip")

rename:
nrg.rename(columns={'NYC Borough, Block, and Lot (BBL)':'BBL'}, 
           inplace=True)
merge:
bblnrgdata = pd.merge(nrg, bsize, how='inner', on=['BBL'])

sfig = scatter_matrix (bblnrgdata, s=300, figsize=(10, 10), diagonal='kde')

drop:
df.drop(['value'], axis=1, inplace=True)

dropping NaN values:
df['value'].dropna(inplace= True)
df['value'].dropna(inplace= True)

plotting histogramswith pandas:
bins = np.arange(10, 99, 5)
axM = df.ageM.groupby(pd.cut(df.ageM, bins)).agg([count_nonzero]).plot(kind='bar', 
                                                                legend=False)
axM.set_title("male riders")
axF = df.ageF.groupby(pd.cut(df.ageF, bins)).agg([count_nonzero]).plot(kind='bar',
                                                                legend=False)
axF.set_title("female riders")

iterate through rows (e.g. every 200):
df.iloc[::200]

plotting linear regression:
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pylab as plt
%matplotlib inline
data=pd.read_csv("/home/cusp/el2666/Applied_Data_Science/data_hw_3_4.csv")
data.head()
lm = smf.ols(formula='Y ~ x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 + x14 + x15', data = data).fit()
print(lm.summary())
y_fit = lm.predict(data)  
plt.figure(figsize = (8,6))
plt.plot(y_fit,data.Y,'or', markersize = 8) 
plt.plot(y_fit,y_fit,'--b', linewidth = 1)
plt.xlabel('Prediction', fontsize = 16)
plt.ylabel('Observation', fontsize = 16)

figure plot:
fig = pl.figure(figsize = (13,6))

ax1 =fig.add_subplot(121)
for i in range(50):
    ax1.hist(reprRandAll[i,0], bins = np.arange(-10,30,0.5), alpha=0.5)
ax2 =fig.add_subplot(122)
for i in range(50):
    ax2.hist(reprRandAll[i,1], bins = np.arange(-10,30,0.5), alpha=0.5)
ax1.set_ylabel("Number of draws in bin", fontsize = 18)
ax1.set_xlabel("x value", fontsize = 18)
ax1.set_ylabel("Number of draws in bin", fontsize = 18)
ax2.set_xlabel("y value", fontsize = 18)

scatter:
ax_gas = df_gas.plot(x = ' Consumption (therms) ', y = ' Consumption (GJ) ', kind = 'scatter', 
            s = 3, title = "NYC gas Consumption", figsize = (10,10), fontsize = 18)
ax_gas.set_xlabel('Consumption (therms)', fontsize = 20)
ax_gas.set_ylabel('Consumption (GJ)', fontsize = 20)

time series plot:
ax = df_sm.plot(x = 'DateSampled', y = 'Likes/Followers/Visits/Downloads', rot=90, 
                figsize = (10,10), fontsize = 18, 
                title = "NYC Agencies social media activity 2011-08-08 to 2012-12-12")

ax.set_ylabel("Number of", fontsize = 18)
ax.set_xlabel("Date", fontsize = 18)

convert date string to date time objects:
df_sm['DateSampled'] = pd.to_datetime(df_sm['Date Sampled'])

Chi-square distribution
depends on the parameter df: degrees of freedom
dof = mean
variance = 2dof

Stating the Null Hypothesis:
H_0: TimeNew.mean() >= TimeOld.mean()
H_a: TimeNew.mean() < TimeOld.mean()
alpha=0.05

the raw input read directly:
!curl -O https://raw.githubusercontent.com/fedhere/PUI2016_fb55/master/Lab3_fb55/times.txt

scatter matrix:
fig = pd.scatter_matrix(allmales['all']
                   [[u'Total with Income',u'$2,500 to $4,999',
                     u'Median income',u'Gini ratio']],
                   linewidth= 3, s=500, figsize=(15,15), 
                        diagonal='kde')   

read json:
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


def get_jsonparsed_data(url):
    """
    from http://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    Receive the content of ``url``, parse it as JSON and return the object.
    Parameters
    ----------
    url : str
    Returns
    -------
    dict
    """
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

plot:
ax = bblnrgdata.plot(kind='scatter',x='nrg',y='UnitsTotal',
                     marker='o', figsize=(10, 10),  
                     xlim=(1000,1e11), ylim=(1,1000), fontsize=22)
yl = ax.set_ylabel("Number of Units in Building", fontsize=20)
xl = ax.set_xlabel("Energy consumption per building (kBtu)", fontsize=20)

plotting standard deviation, error, other:
x = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
y = np.array([3614, 3593, 3510, 4187, 4299, 4126, 4741, 4501, 4371, 5094, 4291, 4582, 4086, 3383, 3125, 2213])
ymean = 3982.25
std = 688.9753715
error = std

ymin = y - std
ymax = y + std

plt.title('Time Series', fontsize=18)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Number', fontsize=14)

plt.plot(x,y)
plt.fill_between(x, ymax, ymin, alpha=0.3)
plt.show()

statistical tests:
p-value: For typical analysis, using the standard α = 0.05 cutoff, the null hypothesis is rejected when p < .05 and not rejected when p > .05. The p-value does not in itself support reasoning about the probabilities of hypotheses but is only a tool for deciding whether to reject the null hypothesis.
Student's t-test of two independent samples: It can be used to determine if two sets of data are significantly different from each other.
>>> stats.ttest_ind(rvs1,rvs2)
(0.26833823296239279, 0.78849443369564776)

reference for different stat tests:
https://docs.scipy.org/doc/scipy/reference/stats.html

chi-square of goodness of fit:
http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-25-chi.html

df.describe()
describe() function would provide count, mean, standard deviation (std), min, quartiles and max in its output 

distribution analysis - histogram:
df['ApplicantIncome'].hist(bins=50)

stacked chart:
temp3 = pd.crosstab(df['Credit_History'], df['Loan_Status'])
temp3.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)

check missing values:
df.apply(lambda x: sum(x.isnull()),axis=0) 
 
fill in missing values - by providing the mean:
df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)

log transformation to nullify effect of outliers:
df['LoanAmount_log'].hist(bins=20)

boxplot - outliers:
import matplotlib.pyplot as plt
%matplotlib inline
data.boxplot(column="ApplicantIncome",by="Loan_Status")

histogram:
data.hist(column="ApplicantIncome",by="Loan_Status",bins=30)

