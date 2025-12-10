# Chicago Taxi Trip Prediction - Vertex AI DEMO4

This repository contains the artifacts for "The partner’s Machine Learning - Services Specialization" demostrating an end-to-end Machine Learning (MLOps) pipeline.

#Description
The objective of this project is to predit the taxi trip duration in Chicago to improve the Estimated Time of Arrival (ETA) service. The solution utilizes public data from BigQuery and trains a Machine Learning model using Vertex AI infrastructure.

## Architecture
The solution leverages the followung Google Cloud services:
** Big Query **: Data Warehousing, cleaning and Feature Engineering
** Verted AI Workbench **: Development environment (Colab Enterprise)
** Vertex AI Training **: Servless custom jobs for model training (Scikit-learn RandomForest)
** Vertex AI Endpoints**: Scalable, real-time serving infrastructure (REST API).

## Files
* Demo4_AI.ipynb: Main notebook containing Exploratory Data Analysis, Pipeline orchestration and deployment logic
* train.py: Modularized Python script used for the remote training job on Vertex AI.
* requirements.txt: List of project dependencies and libraries.

## USAGE
1. ** Data Preparation **: The pipeline pulls data from the public 'chicago_taxi_trips' dataset in BigQuery
2. ** Feature Engineering & Analysis **: Exploratory analysis and data transformation directly within the notebook
3. ** Training & Evaluation **: A RandomForest model is trained and evaluated (RMSE calculation) using scikit-learn.
4. ** Deployment **: The trained model is uploaded to the Registry and deployed to a Vertex AI Endpoint for real-time predictions

## Results
The model is successfully deployed and active on a Vertex AI Endpoint, achieving a baseline RMSE of 8 minutes on the test dataset

## Note on Execution
** Interactive Approach **: Due to the demostration nature of this assessment, the end-to-end workflow (including training) is executed interactively within the `DEMO4_AI.ipnb`
notebook using Vertex AI Colab.
** Reference Script **: The `train.py` file is provided as a reference implementation for modularizing the training logic, intended for potential migration to Vertex AI Pipelines or Custom Jobs

## Code Ownership
This code is Axmos property 
