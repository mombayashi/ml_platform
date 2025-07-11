import pandas as pd
import os
import joblib
from statsmodels.tsa.arima.model import ARIMA

class TimeSeriesModel:
    def __init__(self, model_path="models/timeseries_model.pkl"):
        self.model_path = model_path
        self.model = None

    def train(self, series: pd.Series):
        self.model = ARIMA(series, order=(5, 1, 0)).fit()
        joblib.dump(self.model, self.model_path)

    def load(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            raise FileNotFoundError("時系列モデルが見つかりません")

    def forecast(self, steps: int = 5):
        return self.model.forecast(steps=steps).tolist()
