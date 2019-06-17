import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_csv('EXCL.JK.csv',parse_dates=['Date'])
df2=pd.read_csv('FREN.JK.csv',parse_dates=['Date'])
df3=pd.read_csv('ISAT.JK.csv',parse_dates=['Date'])
df4=pd.read_csv('TLKM.JK.csv',parse_dates=['Date'])

print(df1)

plt.figure('Harga Historis Saham Provider Telco Indonesia')
plt.style.use('bmh')
plt.plot(df1['Date'],df1['Close'],'r-')
plt.plot(df2['Date'],df2['Close'],'g-')
plt.plot(df3['Date'],df3['Close'],'b-')
plt.plot(df4['Date'],df4['Close'],'-')
plt.xticks(rotation=45)
plt.yticks(np.arange(0,4500,step=500))
plt.MaxNLocator(14)
plt.title('Harga Historis Saham Provider Telco Indonesia')
plt.legend(['PT XL Axiata Tbk','PT Smartfren Telecom Tbk','PT Indosat Tbk','PT Telekomunikasi Indonesia Tbk'],loc=6)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')

df1=df1.set_index('Date')
df2=df2.set_index('Date')
df3=df3.set_index('Date')
df4=df4.set_index('Date')
plt.figure('Harga Historis Saham Provider Telco Indonesia (April 2019)')
plt.style.use('bmh')
plt.plot(df1['04-2019'].index,df1['04-2019']['Close'],'r-')
plt.plot(df2['04-2019'].index,df2['04-2019']['Close'],'g-')
plt.plot(df3['04-2019'].index,df3['04-2019']['Close'],'b-')
plt.plot(df4['04-2019'].index,df4['04-2019']['Close'],'-')
plt.xticks(rotation=45)
plt.yticks(np.arange(0,4500,step=500))
plt.title('Harga Historis Saham Provider Telco Indonesia (April 2019)')
plt.legend(['PT XL Axiata Tbk','PT Smartfren Telecom Tbk','PT Indosat Tbk','PT Telekomunikasi Indonesia Tbk'],loc=6)
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')

plt.show()