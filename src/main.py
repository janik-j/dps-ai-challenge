import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
from data.data_utils import load_and_filter_data, visualise_data, create_features
from model.XGBRegressor import train_model

def main(category, scope, predict):
    csv_filepath = os.path.join('data', 'monthly_traffic_accidents.csv')
    
    FEATURES = ['year', 'month']
    TARGET = 'value'

    # Load and filter data
    train = create_features(load_and_filter_data(csv_filepath, 2000, 2020, category=category, scope=scope))
    test = create_features(load_and_filter_data(csv_filepath, 2021, 2022, category=category, scope=scope))

    X_train = train[FEATURES]
    y_train = train[TARGET]

    X_test = test[FEATURES]
    y_test = test[TARGET]

    visualise_data(train, test, title=f'Traffic accidents over time for category {category}', category=category)

    if predict == 'Yes':
        model = train_model(X_train, y_train)
        test['prediction'] = model.predict(X_test)

        visualise_data(train, test, title=f'Raw data and predictions for category {category}', category=category, start_date='2021-01-01', end_date='2023-01-01')

        score = np.sqrt(mean_squared_error(y_test, test['prediction']))
        print(f'RMSE Score on Test set for category {category}: {score:0.2f}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train a model for traffic accidents data.')
    parser.add_argument('--category', type=str, required=True, choices=['Alkoholunfälle', 'Fluchtunfälle', 'Verkehrsunfälle'],
                        help="The category to filter the data on.")
    parser.add_argument('--scope', type=str, required=True,  choices=['insgesamt', 'Verletzte und Getötete', 'mit Personenschäden'],
                        help="The type of the data to filter on.")
    parser.add_argument('--predict', type=str, required=True, choices=['Yes', 'No'],
                        help="Do you want to predict based on the data or just create a visualization?")
    args = parser.parse_args()
    main(args.category, args.scope, args.predict)