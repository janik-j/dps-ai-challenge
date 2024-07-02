import xgboost as xgb
import joblib
import os 

def train_model(X_train, y_train):
    reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree',    
                        n_estimators=5000,
                        max_depth=3,
                        early_stopping_rounds=50,
                        objective='reg:linear',
                        learning_rate=1e-1)
    reg.fit(X_train, y_train,
            eval_set=[(X_train, y_train)],
            verbose=100)
    
    checkpoint_dir = 'checkpoint'
    os.makedirs(checkpoint_dir, exist_ok=True)
    
    # Save the model
    model_path = os.path.join(checkpoint_dir, 'xgb_model.joblib')
    joblib.dump(reg, model_path)

    return reg

