"""
Optional deep-learning extension using TensorFlow.
Run after: pip install tensorflow pandas numpy scikit-learn matplotlib
     python python/beam_deep_learning.py

Uses formula-generated data; validate with experimental data before engineering use.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

rng = np.random.default_rng(7)
n = 5000
kind = rng.integers(0, 2, n)
P = rng.uniform(50, 5000, n)
L = rng.uniform(0.2, 5.0, n)
E_GPa = rng.uniform(60, 210, n)
I_mm4 = rng.uniform(1e4, 5e6, n)
E, I = E_GPa * 1e9, I_mm4 * 1e-12
d_mm = (P * L**3 / (np.where(kind == 0, 48.0, 3.0) * E * I)) * 1000
X = np.column_stack([kind, P, L, E_GPa, I_mm4]).astype("float32")
y = d_mm.astype("float32").reshape(-1, 1)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
Xtr = scaler.fit_transform(Xtr).astype("float32")
Xte = scaler.transform(Xte).astype("float32")

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(5,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer="adam", loss="mse", metrics=["mae"])
model.fit(Xtr, ytr, validation_split=0.2, epochs=40, batch_size=64, verbose=1)
pred = model.predict(Xte, verbose=0).ravel()
print(f"Test MAE: {mean_absolute_error(yte.ravel(), pred):.6f} mm")
print(f"Test R²:  {r2_score(yte.ravel(), pred):.5f}")
Path("outputs").mkdir(exist_ok=True)
model.save("outputs/beam_deflection_nn.keras")
print("Saved model: outputs/beam_deflection_nn.keras")
