# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Trains ML model using training dataset and evaluates using test dataset. Saves trained model.
"""

import argparse
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

def parse_args():
    '''Parse input arguments'''

    parser = argparse.ArgumentParser("train")
    
    # -------- WRITE YOUR CODE HERE --------
    
    # Step 1: Define arguments for train data, test data, model output, and RandomForest hyperparameters. Specify their types and defaults.  


    args = parser.parse_args()

    return args

def main(args):
    '''Read train and test datasets, train model, evaluate model, save trained model'''

    # -------- WRITE YOUR CODE HERE --------

    # Step 2: Read the train and test datasets from the provided paths using pandas. Replace '_______' with appropriate file paths and methods.  
    # Step 3: Split the data into features (X) and target (y) for both train and test datasets. Specify the target column name.  
    # Step 4: Initialize the RandomForest Regressor with specified hyperparameters, and train the model using the training data.  
    # Step 5: Log model hyperparameters like 'n_estimators' and 'max_depth' for tracking purposes in MLflow.  
    # Step 6: Predict target values on the test dataset using the trained model, and calculate the mean squared error.  
    # Step 7: Log the MSE metric in MLflow for model evaluation, and save the trained model to the specified output path.  


if __name__ == "__main__":
    
    mlflow.start_run()

    # Parse Arguments
    args = parse_args()

    lines = [
        f"Train dataset input path: {args.train_data}",
        f"Test dataset input path: {args.test_data}",
        f"Model output path: {args.model_output}",
        f"Number of Estimators: {args.n_estimators}",
        f"Max Depth: {args.max_depth}"
    ]

    for line in lines:
        print(line)

    main(args)

    mlflow.end_run()

