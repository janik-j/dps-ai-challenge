import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List
from datetime import datetime


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