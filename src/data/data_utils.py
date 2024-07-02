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
    data = pd.read_csv(filepath)
    data = data[data['MONAT'] != 'Summe']
    data['datetime'] = pd.to_datetime(data['MONAT'], format='%Y%m')
    data = data[(data['datetime'].dt.year >= start_year) & (data['datetime'].dt.year <= end_year)]
    
    return data

def visualise_data(df: pd.DataFrame, title: str = 'Total amount of traffic accidents over time') -> List[str]:
    """
    Visualise the data by plotting the total amount of traffic accidents over time.

    Parameters:
    df (pd.DataFrame): The filtered data.
    title (str): The title of the plot.

    Returns: A list of file paths to the saved plots.
    """

    categories = ['Alkoholunfälle', 'Fluchtunfälle', 'Verkehrsunfälle']
    df = df[df['AUSPRAEGUNG'] == 'insgesamt']
    pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)

    created_files = []  

    for category in categories:
        df_category = df[df['MONATSZAHL'] == category]
        
        # Splitting the data
        train = df_category[:'2020']
        test = df_category['2021':]
        
        plt.figure(figsize=(15, 5))
        plt.plot(train.index, train['WERT'], '.', label='Train Set', color='blue')
        plt.plot(test.index, test['WERT'], '.', label='Test Set', color='red')
        if not train.empty and not test.empty:
            split_date = pd.Timestamp('2021-01-01')
            plt.axvline(x=split_date, color='black', linestyle='--', label='Train/Test Split')
        plt.title(f'{title} - {category}')
        plt.legend()
        
        file_path = os.path.join("media", f'{category}.png')
        plt.savefig(file_path)
        plt.close()
        created_files.append(file_path)  
    
    return created_files