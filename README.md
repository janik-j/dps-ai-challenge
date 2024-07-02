# dps-ai-challenge
## Project Overview
This repository contains my solution for the Digital Product School AI Engineering Challenge. The project focuses on analyzing and predicting traffic accident data for Munich.
## Dataset
The analysis uses the ["Monatszahlen Verkehrsunfälle"](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7) dataset from the München Open Data Portal. It contains monthly traffic accident statistics for various categories.

## Project Structure
- `api/`: Flask API to deploy the model, also contains subfolder `checkpoints/` with model weights
- `data/`: Contains the raw and processed datasets
- `media/`: Plot visualisations of the data
- `src/`: Source code for data processing, analysis and model training

## Getting Started
To get started with the dps-ai-challenge, follow these steps:

1. Clone the repository: git clone https://github.com/janik-j/dps-ai-challenge.git
2. Install the required dependencies: `pip install -r requirements.txt`
3. Download ["Monatszahlen Verkehrsunfälle"](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7) dataset from the München Open Data Portal and place it as "monthly_traffic_accidents.csv" in the data folder

## Usage
The main functionality of the project is accessed through the `main.py` script in the `src` directory. You can specify the category and scope of the data you're interested in, and choose whether to generate visualizations or predictions.

### Generating Plots
To generate plots for specific categories and scopes without making predictions, use the following commands:

- For alcohol-related accidents (Alkoholunfälle):. <br>
`python src/main.py --category "Verkehrsunfälle" --scope "insgesamt" --predict "No"`<br>
![Alkoholunfälle Graph](media/Alkoholunfälle_2000-01_2024-01_insgesamt.png)

- For accidents involving fleeing (Fluchtunfälle):. <br>
`python src/main.py --category "Fluchtunfälle" --scope "insgesamt" --predict "No"`<br>
![Fluchtunfälle Graph](media/Fluchtunfälle_2000-01_2024-01_insgesamt.png)

- For general traffic accidents (Verkehrsunfälle):. <br>
`python src/main.py --category "Verkehrsunfälle" --scope "insgesamt" --predict "No"`<br>
![Verkehrsunfälle Graph](media/Verkehrsunfälle_2000-01_2024-01_insgesamt.png)


### Making Predictions
To make predictions for specific categories and scopes on the test set, use the command with `--predict "Yes"`:

- For alcohol-related accidents (Alkoholunfälle):. <br>
`python src/main.py --category "Alkoholunfälle" --scope "insgesamt" --predict "Yes"`<br>
![Alkoholunfälle Prediction Graph](media/Alkoholunfälle_2021-01_2023-01_insgesamt_prediction.png)

- For accidents involving fleeing (Fluchtunfälle):. <br>
`python src/main.py --category "Fluchtunfälle" --scope "insgesamt" --predict "Yes"`<br>
![Fluchtunfälle Prediction Graph](media/Fluchtunfälle_2021-01_2023-01_insgesamt_prediction.png)

- For general traffic accidents (Verkehrsunfälle):. <br>
`python src/main.py --category "Verkehrsunfälle" --scope "insgesamt" --predict "Yes"`<br>
![Verkehrsunfälle Prediction Graph](media/Verkehrsunfälle_2021-01_2023-01_insgesamt_prediction.png)

- It's also possible to change the start and end date e.g. for general traffic accidents (Verkehrsunfälle):. <br>
`python src/main.py --category "Verkehrsunfälle" --scope "insgesamt" --predict "Yes" "2000-01-01" --end_date "2023-01-01"`<br>
![Verkehrsunfälle Prediction Graph](media/Verkehrsunfälle_2000-01_2023-01_insgesamt_prediction.png)

- Or predict not for the whole scope but just "Verletzte und Geötete" <br>
`python src/main.py --category "Verkehrsunfälle" --scope "Verletzte und Geötete" --predict "Yes"`<br>
![Verkehrsunfälle Prediction Graph](media/Alkoholunfälle_2021-01_2023-01_Verletzte_und_Getötete_prediction.png)

## Additional Information

### RMSE
- RMSE Score on the test set for category Alkoholunfälle is 10.19 <br>
- RMSE will be always printed after running the script.

### Model
This project uses an XGBoost regressor for predicting traffic accident data. The model is implemented using the XGBoost library and is configured with specific hyperparameters to optimize performance. Key features include:

Booster type: Gradient Boosted Trees (gbtree)
Number of estimators: 5000
Maximum tree depth: 5
Learning rate: 0.001

The trained model is saved using joblib for easy loading and deployment. The model's checkpoint is stored in the api/checkpoints/ directory.