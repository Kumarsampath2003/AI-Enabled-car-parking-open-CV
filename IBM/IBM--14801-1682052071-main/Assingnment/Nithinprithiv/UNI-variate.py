import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("House Price India.csv"

'''df=df.fillna(0
df=df[:100]
y=[i for i in range(0,21)]
fig=plt.figure(figsize=(8,2))
ax=fig.add_subplot(111)
ax.set(title="Histogram",ylab8el='Price',xlabel='Square feet')
ax.hist(df['Price'])
plt.show()'''

#or
df[['id','Date','number of bedrooms','number of bathrooms','living area','lot area','number of floors','waterfront present','number of views','condition of the house','grade of the house','Area of the house(excluding basement)','Area of the basement','Built Year','Renovation Year','Postal Code','Lattitude','Longitude','living_area_renov','lot_area_renov','Number of schools nearby','Distance from the airport','Price']].describe()
# uni-variate analysis
(sns.histplot(df.Price,kde=True))
plt.show()