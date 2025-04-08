from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from cvzone.ClassificationModule import Classifier
import cv2

# Define the input shape of the images
input_shape = (256, 256, 3)

# Create a Sequential model
model = Sequential()

# Add a convolutional layer with 32 filters, a 3x3 kernel, and ReLU activation
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))

# Add a pooling layer with a 2x2 pool size
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add a second convolutional layer with 64 filters, a 3x3 kernel, and ReLU activation
model.add(Conv2D(64, (3, 3), activation='relu'))

# Add a second pooling layer with a 2x2 pool size
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add a third convolutional layer with 128 filters, a 3x3 kernel, and ReLU activation
model.add(Conv2D(128, (3, 3), activation='relu'))

# Add a third pooling layer with a 2x2 pool size
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add a flatten layer to convert the output from 2D to 1D
model.add(Flatten())

# Add two hidden layers with 512 neurons and ReLU activation
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5)) # Add a dropout layer to prevent overfitting
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

# Add an output layer with softmax activation for classification
model.add(Dense(2, activation='softmax'))

# Compile the model with categorical cross-entropy loss and Adam optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print the summary of the model
model.summary()
model.save('model.h5')
mc=Classifier('keras_model.h5','labels.txt')

if True:
        img=cv2.imread('1.jpg')
        
        p=mc.getPrediction(img)
        
        if p[1]==0:
            print("Bat")
        else:
            print("Bee")
