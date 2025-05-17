# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Prepares raw data and provides training and test datasets.
"""

import argparse
from pathlib import Path
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import mlflow

def parse_args():
    '''Parse input arguments'''

    parser = argparse.__________("prep")  # Create an ArgumentParser object
    parser.add_argument("--raw_data", type=_____, help="Path to raw data")  # Specify the type for raw data (str)
    parser.add_argument("--train_data", type=_____, help="Path to train dataset")  # Specify the type for train data (str)
    parser.add_argument("--test_data", type=_____, help="Path to test dataset")  # Specify the type for test data (str)
    parser.add_argument("--test_train_ratio", type=______, default=_____, help="Test-train ratio")  # Specify the type (float) and default value (0.2) for test-train ratio
    args = parser.parse_args()

    return args

def main(args):  # Write the function name for the main data preparation logic
    '''Read, preprocess, split, and save datasets'''

    # Reading Data
    df = pd.read_csv(args.raw_data)

    # ------- WRITE YOUR CODE HERE -------

    # Step 1: Perform label encoding to convert categorical features into numerical values for model compatibility.  
    # Step 2: Split the dataset into training and testing sets using train_test_split with specified test size and random state.  
    # Step 3: Save the training and testing datasets as CSV files in separate directories for easier access and organization.  
    # Step 4: Log the number of rows in the training and testing datasets as metrics for tracking and evaluation.  


if __name__ == "__main__":
    mlflow.start_run()

    # Parse Arguments
    args = _______()  # Call the function to parse arguments

    lines = [
        f"Raw data path: {args._______}",  # Print the raw_data path
        f"Train dataset output path: {args._______}",  # Print the train_data path
        f"Test dataset path: {args._______}",  # Print the test_data path
        f"Test-train ratio: {args._______}",  # Print the test_train_ratio
    ]

    for line in lines:
        print(line)
    
    main(args)

    mlflow.end_run()
