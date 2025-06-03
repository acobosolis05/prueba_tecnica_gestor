from pydantic import BaseModel
from typing import Optional

class PredictionSchema(BaseModel):
    autoID: Optional [str] = ''
    SeniorCity: Optional[int] = None
    Partner: str
    Dependents: str
    Service1: str
    Service2: str
    Security: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    Charges: float
    Demand: float
    