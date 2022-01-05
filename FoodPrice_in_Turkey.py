#%%
import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
df.head()

# %%
df=pd.read_excel('FoodPrice_in_Turkey.xls')
df.head()

# %%
df = pd.read_json('FoodPrice_in_Turkey.json')
df.head()

# %%
df=pd.read_hdf('FoodPrice_in_Turkey.hdf')
df.head()

# %%
df = pd.read_html("FoodPrice_in_Turkey.html")
df[0].head()

# %%
