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
                   test : pd.DataFrame, 
                   title: str = 'Total amount of traffic accidents over time'):
    """
    Visualise the data by plotting the total amount of traffic accidents over time.

    Parameters:
    df (pd.DataFrame): The filtered data.
    title (str): The title of the plot.

    Returns: A list of file paths to the saved plots.
    """

    category_mapping = {0 : 'Alkoholunfälle', 1 : 'Fluchtunfälle', 2: 'Verkehrsunfälle'}
    categories = train['category'].unique()
    created_files = []  

    for category in categories:
        train_category = train[train['category'] == category]
        test_category = test[test['category'] == category]

        plt.figure(figsize=(15, 5))
        split_date = pd.Timestamp('2021-01-01')
        plt.axvline(x=split_date, color='black', linestyle='--', label='Train/Test Split')
        plt.title(f'{title} - {category_mapping[category]}')
        plt.legend()
        if 'prediction' in test_category.columns:
            plt.plot(train_category.index, train_category['value'], '.', label='Train Set', color='blue')
            plt.plot(test_category.index, test_category['value'], '.', label='Test Set', color='blue')
            plt.plot(test_category.index, test_category['prediction'], '.', label='Test Prediction', color='orange')
            file_path = os.path.join("media", f'{category_mapping[category]}_prediction.png')
        else:
            plt.plot(train_category.index, train_category['value'], '.', label='Train Set', color='blue')
            plt.plot(test_category.index, test_category['value'], '.', label='Test Set', color='red')
            file_path = os.path.join("media", f'{category_mapping[category]}.png')
        plt.savefig(file_path)
        plt.close()
        created_files.append(file_path)  
    
    return created_files

