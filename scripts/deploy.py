<<<<<<< HEAD
from flask import Flask, request, jsonify
from keras.models import load_model

app = Flask(__name__)

# Chargez le modèle entraîné
model = load_model("my_model.h5")

# Définissez une route pour effectuer des prédictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtenez les données d'image à partir de la requête POST
        image_data = request.files['image'].read()
        
        # Effectuez la prétraitement nécessaire sur l'image (par exemple, redimensionnement et mise à l'échelle)
        # Assurez-vous que le prétraitement correspond à ce que vous avez fait lors de l'entraînement
        
        # Faites la prédiction en utilisant le modèle chargé
        prediction = model.predict(image_data)
        
        # Convertissez les résultats en une réponse JSON
        result = {'prediction': prediction[0]}
        
        return jsonify(result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
=======
from flask import Flask, request, jsonify
from keras.models import load_model

app = Flask(__name__)

# Chargez le modèle entraîné
model = load_model("my_model.h5")

# Définissez une route pour effectuer des prédictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtenez les données d'image à partir de la requête POST
        image_data = request.files['image'].read()
        
        # Effectuez la prétraitement nécessaire sur l'image (par exemple, redimensionnement et mise à l'échelle)
        # Assurez-vous que le prétraitement correspond à ce que vous avez fait lors de l'entraînement
        
        # Faites la prédiction en utilisant le modèle chargé
        prediction = model.predict(image_data)
        
        # Convertissez les résultats en une réponse JSON
        result = {'prediction': prediction[0]}
        
        return jsonify(result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
>>>>>>> a433d1e99c86e690021fb48ea94c6f616f2c131f
    app.run(debug=True)