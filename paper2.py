# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
# print('asd')

# col_list = ["date", "deaths"]
df = pd.read_csv("data.csv",index_col='date', parse_dates=True)

df['moving_average_recoveries_5']=df['active cases'].rolling(5 ,win_type='triang').mean()
df['moving_average_recoveries_10']=df['active cases'].rolling(18 ,win_type='triang').mean()
df['moving_average_recoveries_15']=df['active cases'].rolling(21 ,win_type='triang').mean()

df['active cases'].plot()
df['moving_average_recoveries_5'].plot()
df['moving_average_recoveries_10'].plot()
df['moving_average_recoveries_15'].plot()
plt.legend(["Wighted moving average","5 days", "10 days","15 days"], loc ="lower right")

# df['predicted']=abs(df['deaths']-df['moving_average_recoveries'])
# print(df[['deaths', 'moving_average_recoveries','predicted']].head(20))
plt.grid(True)

# additive = seasonal_decompose(df['recoveries'], model='additive')
# multiplicative = seasonal_decompose(df['recoveries'], model='multiplicative')



# additive.plot()
# multiplicative.plot()
#
plt.xlabel('dates', fontsize=12)
plt.ylabel('Weighted Moving Average Deaths', fontsize=12)
plt.savefig("weighted mv active cases",bbox_inches = 'tight')
# plt.savefig("multiplicative_recoveries_cases",bbox_inches = 'tight')
plt.show()
