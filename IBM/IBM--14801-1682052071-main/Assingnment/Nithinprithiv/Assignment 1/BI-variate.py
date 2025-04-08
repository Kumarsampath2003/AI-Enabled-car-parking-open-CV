import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("House Price India.csv")
df[['id','Date','number of bedrooms','number of bathrooms','living area','lot area','number of floors','waterfront present','number of views','condition of the house','grade of the house','Area of the house(excluding basement)','Area of the basement','Built Year','Renovation Year','Postal Code','Lattitude','Longitude','living_area_renov','lot_area_renov','Number of schools nearby','Distance from the airport','Price']].describe()
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111)
ax.set(title="price vs live_areas",ylabel='Price',xlabel='living area')
Price=df['Price'].tolist()
living_area=df['living area'].tolist()
ax.hist2d(Price,living_area,bins=100)
plt.show()