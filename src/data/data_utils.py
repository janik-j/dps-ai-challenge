import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import List

def load_and_filter_data(filepath : str, start_year : int = 2000, end_year : int = 2024) -> pd.DataFrame:
    """
    Load the data from the given filepath and filter it based on the start and end year.

    Parameters:
    start_year (int): The start year for filtering the data.
    end_year (int): Filter the data untile the end of this year.
    filepath (str): The path to the raw data file.

    Returns:
    pd.DataFrame: The filtered data.
    """

    # Load the data
    df = pd.read_csv(filepath)

    df = df[df['MONAT'] != 'Summe']
    df = df[df['AUSPRAEGUNG'] == 'insgesamt']

    df['datetime'] = pd.to_datetime(df['MONAT'], format='%Y%m')
    df = df[(df['datetime'].dt.year >= start_year) & (df['datetime'].dt.year <= end_year)]
    pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    df.sort_index(inplace=True)

    return df

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create time series features based on timeseries index and the 'MONATSZAHL' column.
    """
    df = df[['MONATSZAHL', 'AUSPRAEGUNG', 'WERT']].copy()
    df['MONAT'] = df.index.month
    df['JAHR'] = df.index.year

    category_mapping = {'Alkoholunfälle': 0, 'Fluchtunfälle': 1, 'Verkehrsunfälle': 2}
    df['MONATSZAHL'] = df['MONATSZAHL'].map(category_mapping)    

    df['AUSPRAEGUNG'], _ = pd.factorize(df['AUSPRAEGUNG'])

    df.rename(columns={
        'MONATSZAHL': 'category',
        'AUSPRAEGUNG': 'type',
        'WERT': 'value',
        'MONAT': 'month',
        'JAHR': 'year',
    }, inplace=True)

    return df


def visualise_data(train: pd.DataFrame, 
                   test: pd.DataFrame, 
                   title: str = 'Total amount of traffic accidents over time',
                   start_date: str = None,
                   end_date: str = None):
    """
    Visualise the data by plotting the total amount of traffic accidents over time for a specific time range.

    Parameters:
    train (pd.DataFrame): The training data subset.
    test (pd.DataFrame): The testing data subset.
    title (str): The title of the plot.
    start_date (str): The start date for the data to be visualized (inclusive).
    end_date (str): The end date for the data to be visualized (inclusive).

    Returns: A list of file paths to the saved plots.
    """

    category_mapping = {0: 'Alkoholunfälle', 1: 'Fluchtunfälle', 2: 'Verkehrsunfälle'}
    categories = train['category'].unique()
    created_files = []

    # Convert start_date and end_date to datetime if they are not None
    if start_date:
        start_date = pd.to_datetime(start_date)
    if end_date:
        end_date = pd.to_datetime(end_date)

import pandas as pd
import matplotlib.pyplot as plt
import os

def visualise_data(train: pd.DataFrame, 
                   test: pd.DataFrame, 
                   title: str = 'Total amount of traffic accidents over time',
                   start_date: str = "2000-01-01",
                   end_date: str = "2030-01-01"):
    """
    Visualise the data by plotting the total amount of traffic accidents over time for a specific time range.

    Parameters:
    train (pd.DataFrame): The training data subset.
    test (pd.DataFrame): The testing data subset.
    title (str): The title of the plot.
    start_date (str): The start date for the data to be visualized (inclusive).
    end_date (str): The end date for the data to be visualized (inclusive).

    Returns: A list of file paths to the saved plots.
    """

    category_mapping = {0: 'Alkoholunfälle', 1: 'Fluchtunfälle', 2: 'Verkehrsunfälle'}
    categories = train['category'].unique()
    created_files = []

    # Convert start_date and end_date to datetime if they are not None
    if start_date:
        start_date = pd.to_datetime(start_date)
    if end_date:
        end_date = pd.to_datetime(end_date)

    for category in categories:
        train_category = train[train['category'] == category]
        test_category = test[test['category'] == category]

        train_category = train_category[train_category.index >= start_date]
        test_category = test_category[test_category.index >= start_date]
        train_category = train_category[train_category.index <= end_date]
        test_category = test_category[test_category.index <= end_date]

        start_date_str = start_date.strftime('%Y-%m')
        end_date_str = end_date.strftime('%Y-%m')

        plt.figure(figsize=(15, 5))
        split_date = pd.Timestamp('2021-01-01')
        plt.axvline(x=split_date, color='black', linestyle='--', label='Train/Test Split')
        plt.title(f'{title} - {category_mapping[category]}')
        plt.legend()
        if 'prediction' in test_category.columns:
            plt.plot(train_category.index, train_category['value'], '-', label='Train Set', color='blue')
            plt.plot(test_category.index, test_category['value'], '-', label='Test Set', color='blue')
            plt.plot(test_category.index, test_category['prediction'], '-', label='Test Prediction', color='orange')
            file_path = os.path.join("media", f'{category_mapping[category]}_{start_date_str}_{end_date_str}_prediction.png')
        else:
            plt.plot(train_category.index, train_category['value'], '-', label='Train Set', color='blue')
            plt.plot(test_category.index, test_category['value'], '-', label='Test Set', color='red')
            file_path = os.path.join("media", f'{category_mapping[category]}_{start_date_str}_{end_date_str}.png')
        plt.savefig(file_path)
        plt.close()
        created_files.append(file_path)

    return created_files
