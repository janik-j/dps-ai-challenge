import xgboost as xgb
import pandas as pd
import matplotlib.pyplot as plt

def train_model(X_train, y_train):
    reg = xgb.XGBRegressor(n_estimators=1000, learning_rate=1e-1)
    reg.fit(X_train, y_train, verbose=100)
    return reg

