# Progetto_KNN
To read the README.md in Italian, click [here](README_ita.md).

## Index
- [Machine Learning Classifier for Tumor Classification](#machine-learning-classifier-for-tumor-classification)
- [Enviroment set up](#enviroment-set-up)
- [Overview](#overview)
- [Input Requirements](#input-requirements)
- [Output](#output)

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
In this section, we describe the data preprocessing steps involved in our pipeline. There are four files in this section, which are now located within a folder named "Preprocessing." These files facilitate data loading, ensuring it's in CSV format, and handle missing values through various methods (deletion, mean, mode, and median) chosen by user input. Once completed, the data is split into features and labels, followed by feature normalization.

Files in this Section:

preprocessing/ReaderCSV.py  
preprocessing/ReaderFactory.py  
preprocessing/DFInputer.py  
preprocessing/F_and_L.py  

These preprocessing steps are crucial for preparing the dataset before training the machine learning model. They help ensure data integrity and improve the model's performance.

### Model Development 
In this section, we outline the model development process, focusing on the creation of a k-nearest neighbors (k-NN) classifier implemented in a single file. The files in this section are now located within a folder named "KNNalgorithm"

Files in this Section:

KNNalgorithm/KNN.py

This file encapsulates the core logic of the k-NN classifier and serves as the backbone of our model development process. Feel free to explore and extend this implementation to suit your specific requirements. 

### Model Evalutation 
In this section, we elaborate on the model evaluation process, including data splitting, evaluation metrics computation, and the chosen method for validation. The files in this section are now located within a folder named "Evaluation."

Files in this Section:

Evaluation/Evaluation.py  
Evaluation/Metriche_L.py  
Evaluation/Split_Data.py

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

During program execution, various metrics are calculated to evaluate the classification model's performance. Below are the metrics calculated on a sample dataset ('breast_cancer.csv'):

1. Accuracy Rate: This metric measures the percentage of correct predictions compared to the total predictions made by the model. In other words, it represents the overall precision of the model in correctly classifying dataset instances.

2. Error Rate: This metric measures the percentage of incorrect predictions compared to the total predictions made by the model. It complements the Accuracy Rate and provides a measure of the percentage of errors in the model's classifications.

3. Sensitivity: Also known as the True Positive Rate (TPR), this metric measures the model's ability to correctly identify positive instances (class of interest) compared to the total positive instances in the dataset. It indicates the proportion of true positives compared to the total true positives.

4. Specificity: Also known as the True Negative Rate (TNR), this metric measures the model's ability to correctly identify negative instances compared to the total negative instances in the dataset. It indicates the proportion of true negatives compared to the total true negatives.

5. Geometric Mean: This metric calculates the square root of the product of Sensitivity and Specificity. It is a measure of the geometric mean between these two metrics and is used to evaluate the balance between the model's ability to correctly predict positive and negative values. A high Geometric Mean indicates a good balance between Sensitivity and Specificity.

All these metrics provide a comprehensive overview of the classification model's performance and are used to evaluate different aspects of its predictive ability. Additionally, there are graphs available that show the trend of metrics during the evaluation experiments. For example: the holdout metrics graph shows the distribution of metrics for a single experiment through a bar graph of the requested metrics; while the leave-p-out metrics graph shows the trend of metrics over multiple experiments, and there is also a bar graph showing the average of all metrics for all experiments.

### Changes and Variations in Parameters
The outputs described above could vary depending on how input parameters are entered by the user. Those that could bring about significant changes in the output of the classification model could be the k for the KNN neighbors study and the K to define the number of experiments to be run in the Leave_P_Out.

-Varying k for KNN Neighbors, which determines the number of neighbors to consider during the classification of a point, can influence the complexity of the model and, consequently, the classification performance.

   1. By reducing the value of k, the model could become more sensitive to local data details. This could lead to greater variation in predictions, especially in the presence of noisy data or many outliers.
   
   2. By increasing the value of k, the model tends to generalize more. In other words, the model makes decisions based on a larger number of data points, which would make the model less sensitive to local details, leading to a dilution of decision boundaries between classes, thus compromising the model's performance on more complex and/or noisy data.

-Varying K, i.e., the number of Experiments to be run during leave-p-out cross-validation, could affect the robustness of the model evaluation.

   1. By reducing the number of experiments, you get an estimate of the model's performance based on fewer dataset subdivisions. This could lead to greater variance in the estimates of evaluation metrics, as they are based on a smaller sample of data.
   
   2. By increasing the number of experiments, you get a more robust estimate of the model's performance, based on a greater number of dataset subdivisions. This could lead to greater stability in the estimates of evaluation metrics, reducing the uncertainty due to variability in training and test data.

## Plots
The graph illustrates the performance metrics obtained from leave-P-out cross-validation with 500 experiments:
<img width="1528" alt="Andamento Metriche" src="https://github.com/Digre001/Progetto_KNN/assets/149874759/2d817625-9632-40f9-b356-7b13a1540ebe">

The graph displays the average performance metrics derived from leave-P-out cross-validation with 500 experiments.
<img width="1422" alt="Media Metriche" src="https://github.com/Digre001/Progetto_KNN/assets/149874759/9dcdeccf-677c-49c7-aa49-7feb9e906563">

The graph illustrates the performance metrics obtained from the holdout method with a train size of 0.8:
<img width="1271" alt="Metriche Holdout" src="https://github.com/Digre001/Progetto_KNN/assets/149874759/67542083-ba19-4c28-827a-aa890cac9661">









