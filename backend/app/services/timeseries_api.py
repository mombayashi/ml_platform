from typing import List
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_timeseries(data: List[float], forecast_periods: int = 5) -> List[float]:
    """
    シンプルなホルトウィンター法を使って時系列予測を行う関数
    
    Args:
        data: 過去の時系列データのリスト
        forecast_periods: 予測したい未来の期間数（デフォルト5）
    
    Returns:
        予測結果のリスト（forecast_periods分）
    """
    if len(data) < 3:
        raise ValueError("時系列データは最低3点以上必要です。")
    
    series = pd.Series(data)
    model = ExponentialSmoothing(series, trend="add", seasonal=None)
    model_fit = model.fit()
    forecast = model_fit.forecast(forecast_periods)
    return forecast.tolist()
