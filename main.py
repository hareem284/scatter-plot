import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
#reading csv file
df=pd.read_csv("usa.csv")
print(df.info())
print(df.describe())
sns.pairplot(df)
plt.show()