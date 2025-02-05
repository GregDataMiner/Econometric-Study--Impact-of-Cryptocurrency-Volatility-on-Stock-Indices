from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from matplotlib import pyplot as plt

%matplotlib inline

import numpy as np
import pandas as pd
import statsmodels.api as sm
bitcoindata = pd.read_excel("C:/Users/grego/Downloads/bitcoinity_dataF.xlsx")

bitcoindata.head()
bitcoindata.bfill(inplace=True)
bitcoindata.ffill(inplace=True)
bitcoindata['LNS2F']=np.log(bitcoindata['S2F'])

bitcoindata.head()

from IPython.display import set_matplotlib_formats
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

set_matplotlib_formats('retina')
y= bitcoindata['lnprice']
x = pd.to_datetime(bitcoindata['Time'])
plt.title('Ln(price) vs time');
plt.ylabel('ln(price)');
plt.xlabel('time');
plt.plot(x,y);
plt.show();


y= bitcoindata['LNS2F']
x = pd.to_datetime(bitcoindata['Time'])
plt.plot(x,y);
plt.title('Ln(S2F) vs time');
plt.ylabel('ln(S2F)');
plt.xlabel('time');
plt.show();


y=bitcoindata['lnprice']
x=bitcoindata['LNS2F']
plt.scatter(x,y,s=1);
plt.show();


diff1lnprice = bitcoindata['lnprice'].diff()
y= diff1lnprice
x = pd.to_datetime(bitcoindata['Time'])
plt.plot(x,y)
plt.title('First order difference of LN(bitcoin price)');
plt.ylabel('diff1(lnprice)');
plt.xlabel('time');
plt.show();

diff1lnS2F = bitcoindata['LNS2F'].diff()
y= diff1lnS2F
x = pd.to_datetime(bitcoindata['Time'])
plt.title('First order difference of LN(S2F)');
plt.ylabel('diff1(lnprice)');
plt.xlabel('time');

plt.plot(x,y);
plt.show();

fig, axs = plt.subplots(2,2);
axs[0, 0].plot(pd.to_datetime(bitcoindata['Time']), bitcoindata['lnprice'])
axs[0, 0].set_title('Ln(Price)');
axs[0, 1].plot(pd.to_datetime(bitcoindata['Time']), diff1lnprice);
axs[0, 1].set_title('First difference of Ln(price)');
axs[1, 0].plot(pd.to_datetime(bitcoindata['Time']), bitcoindata['LNS2F']);
axs[1, 0].set_title('LN(S2F)');
axs[1, 1].plot(pd.to_datetime(bitcoindata['Time']), diff1lnS2F);
axs[1, 1].set_title('First difference of Ln(S2F)');
fig.tight_layout();

from statsmodels.tsa.stattools import adfuller
#First value is NaN so we have to skip it in the test
result = adfuller(diff1lnprice.iloc[1:])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
    
result = adfuller(diff1lnS2F.iloc[1:])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
    
    
X=sm.add_constant(bitcoindata['LNS2F']);
m=sm.OLS(bitcoindata['lnprice'],X);

results = m.fit()

results.summary()

fig, axs = plt.subplots(2,1);

y=results.resid
x= pd.to_datetime(bitcoindata['Time'])
axs[0].scatter(x,y,s=1)
axs[0].set_title('Residuals of OLS Regression over time');
axs[0].set_ylabel('residuals');
axs[0].set_xlabel('time');
y=results.resid
x= results.fittedvalues
axs[1].scatter(x,y,s=1)
axs[1].set_title('Residuals of OLS Regression over fitted values');
axs[1].set_ylabel('residuals');
axs[1].set_xlabel('fitted values');
fig.tight_layout();

sm.stats.stattools.durbin_watson(results.resid,axis=0)

result = adfuller(results.resid)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))

data = pd.DataFrame()
data['x']=bitcoindata['LNS2F']
data['y']=bitcoindata['lnprice']

from statsmodels.tsa.vector_ar.vecm import coint_johansen
cointtest=coint_johansen(data,0,1)

print('Trace Statistic:') 
print(cointtest.lr1) 
print('Critical Values Trace Statistic [90% 95% 99%]:')
print(cointtest.cvt)
print('Maximum Eigenvalue Statistic') 
print(cointtest.lr2)
print('Critical Values Maximum Eigenvalue Statistic [90% 95% 99%]')
print(cointtest.cvm)

fig, axs = plt.subplots(1,1);

y1=results.fittedvalues
y2=bitcoindata['lnprice']
x= pd.to_datetime(bitcoindata['Time'])
axs.plot(x,y1, label='Fitted Values')
axs.plot(x,y2, label='Actual Values')
axs.set_title('Fitted Values vs Actual Values');
axs.set_xlabel('time');
axs.legend(loc='upper left')

fig.tight_layout();

