# Progetto_KNN

## Index
- [Machine Learning Classifier for Tumor Classification](#1-machine-learning-classifier-for-tumor-classification)
- [Enviroment set up](#2-enviroment-set-up)
- [Overview](#3-overview)
- [Input Requirements](#4-input-requirements)
- [Output](#5-output)

## Machine Learning Classifier for Tumor Classification
Welcome to our repository for the development of a machine learning classifier aimed at classifying tumors as benign or malignant based on user-specified features. Our primary goal is to build a robust pipeline that trains and evaluates a model according to the provided characteristics.

## Enviroment set up
Before running the code, it's important to take some precautions and set up your environment properly. Follow these steps:
1. Create a Virtual Environment:
   - Open your terminal or command prompt.
   - Run the following command to create a virtual environment named "venv":` python -m venv venv`
2. Activate the Virtual Environment:
   - If you're using Windows:    `.\venv\Scripts\activate`
   - If you're using Unix or MacOS:    `source ./venv/Scripts/activate`
3. Deactivate the Environment (When Finished):
   - Use the following command to deactivate the virtual environment:    `deactivate`
4. Install Dependencies:
   - After cloning the project and activating the virtual environment, install the required dependencies using:    `pip install -r requirements.txt`
     This command downloads all the non-standard modules required by the application.
5. If your Python version used to generate the virtual environment doesn't contain an updated version of pip, update pip using:  `pip install --upgrade pip `
  
Once you've set up your virtual environment and installed the dependencies, you're ready to run the application. Simply navigate to the `main.py` file and execute it.


## Overview
This project focuses on three main stages:

- Data Preprocessing: We begin by loading the dataset and handling missing values in a manner of our choice. Subsequently, we split the dataset into features (independent variables) and target labels (classes).

- Model Development: Here, we develop a k-nearest neighbors (k-NN) classifier from scratch, avoiding the use of external libraries that already implement the k-NN classifier. The classifier computes the Euclidean distance between each sample in the test set and all samples in the training set to identify the k nearest neighbors. The class for each test sample is determined by the most common label among its k neighbors, with random selection in case of ties.

- Model Evaluation: We evaluate the model's performance through two approaches:
    1. Holdout method, following specified percentages for training and testing data split.
    1. Leave-p-out Cross Validarion, where p samples are left out for testing and the model is trained on the remaining samples, repeating this process for all possible combinations.

### Data Preprocessing
In this section, we describe the data preprocessing steps involved in our pipeline. There are four files in this section, identified by filenames starting with an uppercase "B". These files facilitate data loading, ensuring it's in CSV format, and handle missing values through various methods (deletion, mean, mode, and median) chosen by user input. Once completed, the data is split into features and labels, followed by feature normalization.

Files in this Section:
- B_ReaderCSV.py
- B_ReaderFactory.py
- B_DFInputer.py
- B_F_and_L.py

These preprocessing steps are crucial for preparing the dataset before training the machine learning model. They help ensure data integrity and improve the model's performance.

### Model Development 
This section outlines the model development process, focusing on the creation of a k-nearest neighbors (k-NN) classifier implemented in a single file. The files in this section are identified by filenames starting with an uppercase "C".

Files in this Section:
- C_Development.py

This file encapsulates the core logic of the k-NN classifier and serves as the backbone of our model development process. Feel free to explore and extend this implementation to suit your specific requirements. 

### Model Evalutation 
This section elaborates on the model evaluation process, including data splitting, evaluation metrics computation, and the chosen method for validation. Files in this section are denoted by filenames starting with an uppercase "D".

Files in this Section:
- D_Evalutation.py
- D_Metriche_L.py
- D_Split_Data.py

Ensure that you select the validation method that best suits your requirements and dataset characteristics. Feel free to explore and customize the evaluation metrics and validation techniques as needed for your specific application.

## Input Requirements
Before running the evaluation model, users need to provide certain inputs. Here's a description of the inputs required:
1. Handling of Missing Values (Gestione):
    - Users need to choose an appropriate method for handling missing values:
        - Input: Integer value representing the selected method (e.g., 1 for drop, 2 for mean, etc.).
          
1. Number of Neighbors for KNN (k):
     - Users specify the number of neighbors to consider in the K-nearest neighbors algorithm:
        - Input: Integer value representing the number of neighbors (k).
Evaluation Model Selection (Modello_valutazione):

1. Users select the evaluation model, either Holdout or Leave-p-out Cross Validation:
   - Input: Single character representing the chosen model (H for Holdout, L for Leave-p-out Cross Validation).
     
1. Training Set Size (train_size):
    - For Holdout method, users specify the percentage of the dataset used for training:
        -Input: Float value between 0 and 1 representing the percentage (e.g., 0.7 for 70%).
    -If Leave-p-out Cross Validation is chosen, users specify the number of samples to study:
        - Input: Integer value representing the number of samples (p).
          
1. Number of Experiments for Leave-p-out (N_esperimenti):
    - If Leave-p-out Cross Validation is chosen, users specify the number of experiments to conduct:
        - Input: Integer value representing the number of experiments (K).
          
1. Metrics Selection (Metriche):
    - Users select the evaluation metrics to be used for assessing model performance:
        - Input: Multiple metrics can be chosen based on the implemented function.
Users are prompted to provide these inputs through the provided class methods. Ensure correct inputs are provided to facilitate accurate evaluation of the model's performance.

## Output
