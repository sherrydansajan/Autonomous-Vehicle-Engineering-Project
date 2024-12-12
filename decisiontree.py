# -*- coding: utf-8 -*-
"""Decisiontree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rG4Jnl0ZnEP7FPDSpgaJtIm2q0Zz7DtI
"""

import pickle
import tensorflow as tf
import keras
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from google.colab import drive
import os

root = '/content/drive/'
drive.mount(root)
mnist_path = 'My Drive/Colab Notebooks/IAVPROJECT/'
#output_path = os.path.join(root, mnist_path, 'output')
#model_name = 'digit_classifier.model'
#model_path = os.path.join(output_path, model_name)
dataset_path = os.path.join(root, mnist_path, 'data/Book1.csv')
df = pd.read_csv(dataset_path)
# Load the model from the file
with open('xgboost_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

features = list(df.columns)[:-1]
X= df[features]
# Make predictions using the loaded model
predictions_loaded_model = loaded_model.predict(X)
print(predictions_loaded_model)