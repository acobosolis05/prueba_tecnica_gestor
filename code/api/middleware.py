import logging
from joblib import load
from config.config_file import PATH_SCALER_MODEL, PATH_CLASSIFIER_MODEL, PATH_LABEL_ENCODER_FILE

import pandas as pd
import json


class Middleware:
    def __init__(self):
        
        self.scaler = load(PATH_SCALER_MODEL)
        self.classifier = load(PATH_CLASSIFIER_MODEL)
        logging.info("Middleware initialized with models loaded.")
        

    def preprocess(self, validated_data):
        try:
            logging.info("Starting preprocessing of data.")

            self.df = pd.DataFrame([validated_data.dict()])
            self.df.drop(columns=['autoID', 'SeniorCity'], inplace=True, errors='ignore')

            return self.df
        
        except Exception as e:
            logging.error(f"Error during preprocessing: {e}")
            raise ValueError("Preprocessing failed") from e
    
    def scale_numeric_columns(self):
        try:
            logging.info("Scaling numeric columns.")

            scaled_values = self.scaler.transform(self.df[['Charges', 'Demand']])
            self.df[['Charges', 'Demand']] = scaled_values

            logging.info("Scaling completed successfully.")

            return self.df
        
        except Exception as e:
            logging.error(f"Error during scaling: {e}")
            raise ValueError("Scaling failed") from e
        
    def encode_categorical_columns(self):
        try:
            logging.info("Encoding categorical columns.")

            with open(PATH_LABEL_ENCODER_FILE, 'r') as file:
                label_encoders = json.load(file)

            categorical_columns = ['Partner', 'Dependents', 'Service1', 'Service2', 
                                'Security', 'OnlineBackup', 'DeviceProtection', 
                                'TechSupport', 'Contract', 'PaperlessBilling', 
                                'PaymentMethod']
        
            for col in categorical_columns:
                self.df[col] = self.df[col].map(label_encoders.get(col))

            logging.info("Encoding completed successfully.")
            return self.df
        
        except Exception as e:
            logging.error(f"Error during encoding: {e}")
            raise ValueError("Encoding failed") from e
        
    def predict(self):
        try:
            reverse_mapping = {
                0: 'Alpha',
                1: 'Betha'
            }

            logging.info("Starting prediction.")

            result_classifier = self.classifier.predict(self.df)
            
            logging.info("Prediction completed successfully.")
            
            predicted_class_index = int(result_classifier[0])
            decoded_class = reverse_mapping.get(predicted_class_index, 'Unknown')
            prediction_result = {
                "Class": decoded_class
            }

            return json.dumps(prediction_result)
        
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            raise ValueError("Prediction failed") from e

        
        


        