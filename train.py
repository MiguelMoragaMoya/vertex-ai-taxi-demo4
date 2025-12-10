import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import numpy as np

# Este script refleja la lógica utilizada en el Notebook de la Demo

def train_model(df):
    """
    Entrena el modelo de predicción de tiempos de taxi.
    """
    # 1. Definir columnas (Features y Target)
    cols = ['trip_miles', 'pickup_community_area', 'dropoff_community_area', 'hour_of_day', 'day_of_week']
    target = 'trip_seconds'

    # 2. Preparar datos
    X = df[cols].copy().fillna(0)
    y = df[target].copy()

    # 3. Split
    print("Dividiendo datos...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=14)

    # 4. Entrenar
    print("Entrenando RandomForest (n_estimators=20)...")
    model = RandomForestRegressor(n_estimators=20, max_depth=10, random_state=14)
    model.fit(X_train, y_train)

    # 5. Evaluar
    rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
    print(f"Modelo entrenado. RMSE: {rmse:.2f}")

    # 6. Guardar
    joblib.dump(model, 'model.joblib')
    print("Modelo guardado como model.joblib")

if __name__ == "__main__":
    # Nota: En el notebook, los datos se cargan directamente desde BQ.
    # Aquí dejamos la estructura lista.
    print("Este script contiene la lógica de entrenamiento usada en el Notebook.")
