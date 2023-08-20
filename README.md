# absenteeismapp
The goal of this project is building an application that predicts the absence or presence of a company's employees
This repository contains code for a machine learning model that predicts absenteeism based on various factors. The project includes a custom scaler class and a special class for predicting absenteeism using a trained model.

Project Structure
custom_scaler.py: This file contains the CustomScaler class, a custom implementation of a scaler using StandardScaler from the scikit-learn library.

absenteeism_model.py: This file defines the absenteeism_model class, which is used for loading a trained model and scaler, preprocessing data, and making predictions.

model: The trained model binary file.

scaler: The scaler binary file.

Requirements
Python 3.x
numpy
pandas
scikit-learn

Data Preprocessing
The load_and_clean_data method of the absenteeism_model class preprocesses new data in the following steps:

Drops the 'ID' column.
Creates dummy columns for different reasons for absence.
Extracts month and day of the week information from the 'Date' column.
Maps 'Education' variables to dummies.
Replaces NaN values with 0.
Drops unnecessary columns.
Applies scaling using the previously trained scaler.

Note
This code assumes that you have the trained model and scaler files (model and scaler) available in the same directory as the code files.

Remember to replace 'new_data.csv' in the code snippet with the path to your new data file.

The provided code is a simplified example and might need further adjustments based on your specific use case.

License
This project is licensed under the MIT License.

Feel free to contribute and improve this project. If you encounter any issues or have questions, please create an issue in the repository.
