# AI-BioDiscover
AI/ML Tool for Antibody Design and Molecular Property Prediction

# AI/ML Tool for Antibody Design

## Overview
This project implements an AI/ML tool designed to predict molecular properties based on antibody sequences. By utilizing machine learning techniques, the tool aims to streamline the discovery and development of biologics, particularly in antibody design.

## Features
- **Data Preprocessing**: Cleans and prepares datasets for analysis.
- **Machine Learning Models**: Implements models for molecular property prediction, utilizing Random Forest as a baseline.
- **Exploratory Data Analysis**: Visualizes multi-dimensional datasets to identify trends and insights.
- **Evaluation Metrics**: Calculates model performance using metrics like Mean Squared Error (MSE).
- **Visualization**: Provides graphical representation of model predictions against actual values.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Example](#example)
- [Contributions](#contributions)
- [License](#license)
- [Contact](#contact)

```bash

## Installation
To set up the project, clone this repository and install the required packages:


git clone https://github.com/yourusername/AI_ML_Antibody_Design_Tool.git
cd AI_ML_Antibody_Design_Tool
pip install -r requirements.txt


## Usage
Prepare your dataset in the data directory. The dataset should be in CSV format with columns for antibody sequences and their corresponding properties.
Open the Jupyter notebook located in the notebooks directory: antibody_design_example.ipynb.
Follow the instructions in the notebook to load data, train the model, evaluate performance, and visualize results.

## Data
The example dataset can be found in the data/example_dataset.csv file. This dataset includes sequences of antibodies and a corresponding property score. You can modify this dataset or add your own for testing.

Sample Dataset Format
sequence,property
"ACDEFGHIKLMNPQRSTVWY",0.7
"FGHIKLMNPQRSTVWYACDE",0.65
...

## Example
In the notebooks directory, you will find antibody_design_example.ipynb, which provides a step-by-step guide on using the tool. It covers data loading, preprocessing, model training, evaluation, and visualization of results.

Running the Notebook
To run the Jupyter notebook:

Ensure Jupyter is installed in your Python environment.

Launch Jupyter Notebook:

jupyter notebook


Open antibody_design_example.ipynb and follow the instructions.

## Key Improvements
Multiple Models: The train_model function now supports training different types of models (Random Forest, Linear Regression, and Support Vector Regression).
Hyperparameter Tuning: Users can pass hyperparameters for GridSearchCV to optimize the model.
Additional Evaluation Metrics: The evaluation function now includes Mean Absolute Error (MAE) and R² score along with MSE.
Visualization Improvements: The plotting function uses Seaborn for enhanced visualization.

##Contributions
Contributions are welcome! Please feel free to open issues or submit pull requests. If you have ideas for improvements or features, I'd love to hear them.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
bioinformati84@gmail.com
https://github.com/Mohammad-Vahed
https://www.linkedin.com/in/mohammad-vahed-53485530/
