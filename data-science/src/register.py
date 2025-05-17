# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
Registers the best-trained ML model from the sweep job.
"""

import argparse
from pathlib import Path
import mlflow
import os 
import json

def parse_args():
    '''Parse input arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=_____, help='Name under which model will be registered')  # Hint: Specify the type for model_name (str)
    parser.add_argument('--model_path', type=_____, help='Model directory')  # Hint: Specify the type for model_path (str)
    parser.add_argument("--model_info_output_path", type=_____, help="Path to write model info JSON")  # Hint: Specify the type for model_info_output_path (str)
    args, _ = parser.parse_known_args()
    print(f'Arguments: {args}')

    return args

def main(args):
    '''Loads the best-trained model from the sweep job and registers it'''

    print("Registering ", args.model_name)


    # -----------  WRITE YOR CODE HERE -----------
    
    # Step 1: Load the model from the specified path using `mlflow.sklearn.load_model` for further processing.  
    # Step 2: Log the loaded model in MLflow with the specified model name for versioning and tracking.  
    # Step 3: Register the logged model using its URI and model name, and retrieve its registered version.  
    # Step 4: Write model registration details, including model name and version, into a JSON file in the specified output path.  


if __name__ == "__main__":
    
    mlflow.start_run()
    
    # Parse Arguments
    args = parse_args()
    
    lines = [
        f"Model name: {args.________}",
        f"Model path: {args.________}",
        f"Model info output path: {args.________}"
    ]

    for line in lines:
        print(line)

    main(args)

    mlflow.end_run()