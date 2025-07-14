from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from app.services.timeseries_api import forecast_timeseries

router = APIRouter()


class TimeseriesRequest(BaseModel):
    data: List[float] = Field(description="時系列データのリスト")
    periods: int = Field(description="予測したい期間（ステップ数）")


@router.post("/")
def get_forecast(request: TimeseriesRequest):
    try:
        forecast = forecast_timeseries(request.data, request.periods)
        return {"input_data": request.data, "forecast": forecast}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
