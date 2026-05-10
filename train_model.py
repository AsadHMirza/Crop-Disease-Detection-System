import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout
import matplotlib.pyplot as plt

# =========================
# DATASET PATH
# =========================

dataset_path = "dataset/PlantVillage"

# =========================
# IMAGE PREPROCESSING
# =========================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train_data = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(128,128),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

validation_data = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(128,128),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Print classes
print(train_data.class_indices)

# =========================
# CNN MODEL
# =========================

model = Sequential()

# First Convolution Layer
model.add(Conv2D(
    32,
    (3,3),
    activation='relu',
    input_shape=(128,128,3)
))

model.add(MaxPooling2D(pool_size=(2,2)))

# Second Convolution Layer
model.add(Conv2D(
    64,
    (3,3),
    activation='relu'
))

model.add(MaxPooling2D(pool_size=(2,2)))

# Flatten Layer
model.add(Flatten())

# Dense Layer
model.add(Dense(
    128,
    activation='relu'
))

# Dropout Layer
model.add(Dropout(0.5))

# Output Layer
model.add(Dense(
    train_data.num_classes,
    activation='softmax'
))

# =========================
# COMPILE MODEL
# =========================

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# =========================
# TRAIN MODEL
# =========================

history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=10
)

# =========================
# SAVE MODEL
# =========================

model.save(
    "model/plant_disease_model.h5"
)

print("Model Trained Successfully ✅")

# =========================
# ACCURACY GRAPH
# =========================

plt.plot(history.history['accuracy'])

plt.plot(history.history['val_accuracy'])

plt.title("Model Accuracy")

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.legend(["Training", "Validation"])

plt.show()
