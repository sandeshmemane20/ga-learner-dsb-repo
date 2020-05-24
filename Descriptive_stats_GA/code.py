# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
print(gender_count)
gender_count.plot(kind='bar')
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
#print(alignment)
fig1, ax1 = plt.subplots()
ax1.pie(alignment,  autopct='%1.2f%%', startangle=90,textprops=dict(color="w"))
ax1.axis('equal') 
ax1.legend(alignment.index, title="Alignment",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
ax1.set_title('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().loc['Strength','Combat']
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = round(sc_covariance / (sc_strength*sc_combat),2)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().loc['Intelligence','Combat']
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = sc_df['Combat'].std()
ic_pearson = round(ic_covariance / (ic_intelligence*ic_combat),2)
print(ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)

super_best = data[data['Total']>total_high]

super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here

fig1, (ax_1,ax_2,ax_3) = plt.subplots(1,3,figsize=(14,8))

ax_1.boxplot(data['Intelligence'],labels=['Intelligence'])
ax_2.boxplot(data['Speed'],labels=['Speed'])
ax_3.boxplot(data['Power'],labels=['Power'])


