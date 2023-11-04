<<<<<<< HEAD
import tensorflow as tf
from tensorflow.keras import layers, models

# Création du modèle CNN
model = models.Sequential()

# Couche de convolution 2D
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Autres couches de convolution et de pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Couches fully connected (Dense)
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))  # Couche de sortie pour la classification binaire

# Compilation du modèle
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Résumé du modèle
model.summary()

# Entraînement du modèle
history = model.fit(X_train, y_train_encoded, epochs=10, validation_data=(X_val, y_val_encoded))

# Évaluation du modèle sur les données de test
test_loss, test_acc = model.evaluate(X_test, y_test_encoded)
=======
import tensorflow as tf
from tensorflow.keras import layers, models

# Création du modèle CNN
model = models.Sequential()

# Couche de convolution 2D
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Autres couches de convolution et de pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Couches fully connected (Dense)
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))  # Couche de sortie pour la classification binaire

# Compilation du modèle
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Résumé du modèle
model.summary()

# Entraînement du modèle
history = model.fit(X_train, y_train_encoded, epochs=10, validation_data=(X_val, y_val_encoded))

# Évaluation du modèle sur les données de test
test_loss, test_acc = model.evaluate(X_test, y_test_encoded)
>>>>>>> a433d1e99c86e690021fb48ea94c6f616f2c131f
print(f'Accuracy on test data: {test_acc}')