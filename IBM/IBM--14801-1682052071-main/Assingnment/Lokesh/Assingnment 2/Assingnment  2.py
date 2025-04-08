import numpy as np
import pandas as pd
import tensorflow as tf
from numpy import loadtxt
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense

data = pd.read_csv("House Price India.csv")

# split into input (X) and output (y) variables
x=data.iloc[:,0:2].values
y=data.iloc[:,2].values
#print(x)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

from keras.models import Sequential
from keras.layers import Dense
model=Sequential()

#input Layer
model.add(Dense(2,input_dim=2,activation='relu'))
#hidden Layer
model.add(Dense(2,activation='relu'))
#output layer
                    #...............................only 2 sigmoid ,more than 2 softmax
model.add(Dense(1,activation='sigmoid')) 

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(xtrain,ytrain,epochs=20,batch_size=45)

_,acc=model.evaluate(xtest,ytest)
print("accuracy: ",acc)
i= int (input("wait"))
