"""
Beam Deflection: Data Science, Machine Learning & Visualization
Run: pip install -r requirements.txt
     python python/beam_ml_analysis.py

This creates a synthetic dataset using standard beam-deflection equations.
It is a learning/demo model, not a substitute for engineering validation.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

OUT = Path("outputs")
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(42)
n = 2500

beam_type = rng.integers(0, 2, n)  # 0=simple support, 1=cantilever
P = rng.uniform(50, 5000, n)       # N
L = rng.uniform(0.2, 5.0, n)       # m
E_GPa = rng.uniform(60, 210, n)    # GPa
I_mm4 = rng.uniform(1e4, 5e6, n)   # mm^4
E = E_GPa * 1e9
I = I_mm4 * 1e-12                  # m^4

# Formula: simply supported P*L^3/(48EI); cantilever P*L^3/(3EI)
factor = np.where(beam_type == 0, 48.0, 3.0)
deflection_m = P * L**3 / (factor * E * I)
df = pd.DataFrame({
    "beam_type": beam_type, "load_N": P, "length_m": L,
    "youngs_modulus_GPa": E_GPa, "moment_inertia_mm4": I_mm4,
    "deflection_mm": deflection_m * 1000
})
df.to_csv(OUT / "synthetic_beam_dataset.csv", index=False)

X = df.drop(columns="deflection_mm")
y = df["deflection_mm"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestRegressor(n_estimators=160, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, pred):.6f} mm")
print(f"R²:  {r2_score(y_test, pred):.5f}")
print("Note: model is trained on formula-generated data, not experimental measurements.")

plt.figure()
plt.scatter(y_test, pred, s=12, alpha=0.5)
lo, hi = min(y_test.min(), pred.min()), max(y_test.max(), pred.max())
plt.plot([lo, hi], [lo, hi], linestyle="--")
plt.xlabel("Formula deflection (mm)")
plt.ylabel("ML-predicted deflection (mm)")
plt.title("Beam Deflection: Actual vs ML Prediction")
plt.tight_layout()
plt.savefig(OUT / "actual_vs_predicted.png", dpi=160)
plt.close()

importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()
plt.figure()
importance.plot(kind="barh")
plt.xlabel("Feature importance")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig(OUT / "feature_importance.png", dpi=160)
plt.close()

print(f"Saved dataset and charts to: {OUT.resolve()}")
