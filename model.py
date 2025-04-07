#1. Importar librerías necesarias

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
2. Cargar tus datos

df = pd.read_csv("tus_datos.csv")  # o el archivo que tengas
3. Explorar y limpiar los datos
Verifica valores nulos

Convierte columnas categóricas a numéricas (One-hot u ordinal)

Asegúrate de que los tipos de datos estén bien definidos


df.info()
df.describe()
df.isnull().sum()
df = df.dropna()
4. Seleccionar características (X) y variable objetivo (y)
Supongamos que quieres predecir members:


X = df[['score', 'episodes', 'popularity']]  # tus variables predictoras
y = df['members']  # tu variable objetivo
5. Codificar variables categóricas si las hay

X = pd.get_dummies(X, drop_first=True)
6. Dividir el dataset en entrenamiento y prueba

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
7. Seleccionar y entrenar un modelo

model = LinearRegression()
model.fit(X_train, y_train)
8. Hacer predicciones

y_pred = model.predict(X_test)
9. Evaluar el modelo

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
10. (Opcional) Visualizar resultados

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Valores reales vs Predicciones")
plt.show()
