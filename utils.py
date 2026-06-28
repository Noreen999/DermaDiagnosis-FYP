import json
import numpy as np
from PIL import Image
import tensorflow as tf

# Load JSON class labels
def load_class_labels(json_path):
    with open(json_path, 'r') as f:
        return {int(k): v for k, v in json.load(f).items()}

# Preprocess image
def preprocess_image(image, size=(224, 224)):
    if isinstance(image, str):
        image = Image.open(image)
    image = image.convert('RGB').resize(size)
    img_array = np.array(image)/255.0
    return np.expand_dims(img_array, axis=0)

# Load model safely
def load_model(model_path):
    return tf.keras.models.load_model(model_path)
