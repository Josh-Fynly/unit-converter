# api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from core.conversions import convert_length, convert_weight, convert_temp
from core.exceptions import UnsupportedUnitError, InvalidValueError

app = FastAPI(
    title="Universal Unit Convertly API",
    description="Backend API for unit conversions",
    version="1.0.0"
)


# -------------------
# Request & Response
# -------------------

class ConversionRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str


class ConversionResponse(BaseModel):
    result: float


# -------------------
# Helper Function
# -------------------

def handle_conversion(func, request: ConversionRequest) -> ConversionResponse:
    """
    Runs the conversion function and handles exceptions safely.
    """
    try:
        result = func(request.value, request.from_unit, request.to_unit)
        return ConversionResponse(result=result)

    except InvalidValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except UnsupportedUnitError as e:
        raise HTTPException(status_code=422, detail=str(e))


# -------------------
# API Endpoints
# -------------------

@app.post("/convert/length", response_model=ConversionResponse)
def convert_length_endpoint(request: ConversionRequest):
    return handle_conversion(convert_length, request)


@app.post("/convert/weight", response_model=ConversionResponse)
def convert_weight_endpoint(request: ConversionRequest):
    return handle_conversion(convert_weight, request)


@app.post("/convert/temperature", response_model=ConversionResponse)
def convert_temperature_endpoint(request: ConversionRequest):
    return handle_conversion(convert_temp, request)
