import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("House Price India.csv")
df[['id','Date','number of bedrooms','number of bathrooms','living area','lot area','number of floors','waterfront present','number of views','condition of the house','grade of the house','Area of the house(excluding basement)','Area of the basement','Built Year','Renovation Year','Postal Code','Lattitude','Longitude','living_area_renov','lot_area_renov','Number of schools nearby','Distance from the airport','Price']].describe()
(sns.pairplot(data=df[['id','Date','number of bedrooms','number of bathrooms','living area','Price']],hue="Price"))
plt.show()
