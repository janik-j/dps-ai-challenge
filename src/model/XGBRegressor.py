import xgboost as xgb
import joblib
import os 

def train_model(X_train, y_train):
    reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree',    
                        n_estimators=5000,
                        max_depth=5,
                        learning_rate=1e-3)
    reg.fit(X_train, y_train,
            eval_set=[(X_train, y_train)],
            verbose=100)
    
    model_path = os.path.join('api', 'checkpoints', 'xgb_model.joblib')
    joblib.dump(reg, model_path)

    return reg

