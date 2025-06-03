from fastapi import FastAPI, HTTPException, Request, Response
from schemas.schema_api_prediction import PredictionSchema
from fastapi.responses import JSONResponse
from api.controller import Controller
import logging
import json

app = FastAPI()
@app.post("/predict")
async def predict(request:Request):
    try:
        data = await request.json()
        validated_data = PredictionSchema(**data)
        
        controller = Controller(validated_data)
        result_dict = controller.get_result()


        logging.info(f"Prediction response: {result_dict}")

        return JSONResponse(content=result_dict, status_code=200)
    
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=400, detail=str(e))

        