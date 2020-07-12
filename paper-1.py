# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


# col_list = ["date", "deaths"]
df = pd.read_csv("data.csv",index_col='date', parse_dates=True)

df['moving_average_recoveries']=df['deaths'].rolling(5 ,win_type='triang').mean()
df['deaths'].plot()
df['moving_average_recoveries'].plot()
df['predicted']=abs(df['deaths']-df['moving_average_recoveries'])
print(df[['deaths', 'moving_average_recoveries','predicted']].head(20))
plt.grid(True)

additive = seasonal_decompose(df['recoveries'], model='additive')
multiplicative = seasonal_decompose(df['recoveries'], model='multiplicative')



# additive.plot()
multiplicative.plot()

plt.xlabel('dates', fontsize=12)
plt.ylabel('deaths', fontsize=12)
# plt.savefig("additive_recoveries_cases",bbox_inches = 'tight')
plt.savefig("multiplicative_recoveries_cases",bbox_inches = 'tight')
plt.show()
