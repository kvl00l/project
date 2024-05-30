import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('monthly_sales.csv')

df.head(5)
df.shape
df.describe
df.isnull().sum()

sns.set_palette("husl")
plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='Sales', data=df, marker='o')
plt.grid(True)
plt.show()