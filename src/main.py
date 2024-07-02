import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from data.data_utils import load_and_filter_data, visualise_data, create_features
from model.XGBRegressor import train_model

def main():
    # Path to the raw data file
    csv_filepath = os.path.join('data', 'monthly_traffic_accidents.csv')
    
    train = create_features(load_and_filter_data(csv_filepath, 2000, 2020))
    test = create_features(load_and_filter_data(csv_filepath, 2021, 2022))
    visualise_data(train, test, title='Total amount of traffic accidents over time')
    FEATURES = ['category', 'type', 'year', 'month']
    TARGET = 'value'

    X_train = train[FEATURES]
    y_train = train[TARGET]

    X_test = test[FEATURES]
    y_test = test[TARGET]

    model = train_model(X_train, y_train)
    test['prediction'] = model.predict(X_test)
    print(test.head(40))
    visualise_data(train, test, title='Raw data and predictions', start_date='2021-01-01', end_date='2022-01-01')


if __name__ == '__main__':
    main()
