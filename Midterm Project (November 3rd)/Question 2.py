import pandas as pd
import matplotlib.pyplot as plt
import json

df = pd.read_csv('amazon_report.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = df.fillna(0)
df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)

#Total
print('The total amount spent: ', df["Total Charged"].sum())
print('The mean amount spent: ', df["Total Charged"].mean())
print('The median amount spent: ', df["Total Charged"].median())
print('The maximum amount spent: ', df["Total Charged"].max())
print('The minimum amount spent: ', df["Total Charged"].min())

#Taxes
df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
print('The overall effectice sales tax paid: ', df["Tax Charged"].sum() / df["Total Charged"].sum(), 'or 5.51%')
print('The total sales tax paid: ', df["Tax Charged"].sum())

#Orders
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.plot.bar(x='Order Date', y='Total Charged', rot=90, figsize=(10,20), color='#61D199')
plt.title("Daniel's Amazon Spending 2020-2021")
plt.ylabel('Amount spent in $')

daily_orders = df.groupby('Order Date').sum()["Total Charged"]
print(daily_orders.head())
print(daily_orders.plot.bar(figsize=(10,20), color='#61D199'))

plt.show()

print(df.head())
