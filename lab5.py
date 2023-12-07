import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.set(font_scale=1.3)
df = pd.read_csv('5лаба.csv', delimiter=';')
df = df.drop(columns=['<TICKER>', '<PER>', '<TIME>', '<VOL>'], axis=1)
df1 = df[df['<DATE>'] == '03.09.2018']
sns.boxplot(
    data=df1)
plt.yticks(np.arange(106000,110000,500))
plt.show()
df2 = df[df['<DATE>'] == '03.10.2018']
sns.boxplot(
    data=df2)
plt.yticks(np.arange(114000,120000,500))
plt.show()
df3 = df[df['<DATE>'] == '07.11.2018']
sns.boxplot(
    data=df3)
plt.yticks(np.arange(112000,118000,500))
plt.show()
df4 = df[df['<DATE>'] == '03.12.2018']
sns.boxplot(
    data=df4)
plt.yticks(np.arange(110500,118000,500))
plt.show()