import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from data.data_utils import load_and_filter_data, visualise_data

def main():
    # Path to the raw data file
    csv_filepath = os.path.join('data', 'monthly_traffic_accidents.csv')
    # Process and save data
    df = load_and_filter_data(csv_filepath, 2000, 2024)
    print(visualise_data(df))


if __name__ == '__main__':
    main()
