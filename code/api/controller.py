import logging
import json
from api.middleware import Middleware
from schemas.schema_api_prediction import PredictionSchema

class Controller:
    
    def __init__(self, validated_data: PredictionSchema):

        self.middleware = Middleware()
        self.middleware.preprocess(validated_data)
        self.middleware.scale_numeric_columns()
        self.middleware.encode_categorical_columns()
        json_output = self.middleware.predict()
        
        try:
            
            self.result = json.loads(json_output)
        except (TypeError, json.JSONDecodeError):
            
            self.result = json_output

        logging.info(f"Controller initialized, prediction result: {self.result}")

        

    def get_result(self) -> dict:
        """
        Devuelve un diccionario con el resultado de la predicción.
        """
        return self.result