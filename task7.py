# -*- coding: utf-8 -*-
"""task7

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19wx7PBQbwUbFTsYpzfnd9jaqvWGNhvGv
"""

import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target

# Display the first few rows of the dataset
print(data.head())

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Split the dataset into features and target
X = data.drop('species', axis=1)
y = data['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

import seaborn as sns
import matplotlib.pyplot as plt

# Pairplot to visualize the relationships between features
sns.pairplot(data, hue='species')
plt.show()

# Display correlation matrix
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Initialize the models
svc_model = SVC(kernel='linear')
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the models
svc_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)

# Predict using the trained models
svc_predictions = svc_model.predict(X_test)
rf_predictions = rf_model.predict(X_test)

# Evaluate the models
svc_accuracy = accuracy_score(y_test, svc_predictions)
rf_accuracy = accuracy_score(y_test, rf_predictions)

print(f"SVM Accuracy: {svc_accuracy}")
print(f"Random Forest Accuracy: {rf_accuracy}")

import joblib

# Save the RandomForest model
joblib.dump(rf_model, 'rf_model.pkl')

# Load the model (for later use)
loaded_rf_model = joblib.load('rf_model.pkl')

# Test the loaded model
loaded_rf_predictions = loaded_rf_model.predict(X_test)
loaded_rf_accuracy = accuracy_score(y_test, loaded_rf_predictions)
print(f"Loaded RF Model Accuracy: {loaded_rf_accuracy}")







