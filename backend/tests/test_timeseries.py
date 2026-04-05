import pytest
from app.services.timeseries_api import forecast_timeseries


def test_forecast_returns_correct_length():
    data = [100.0, 102.0, 104.0, 103.0, 105.0]
    result = forecast_timeseries(data, forecast_periods=3)
    assert len(result) == 3


def test_forecast_returns_floats():
    data = [10.0, 20.0, 30.0, 40.0, 50.0]
    result = forecast_timeseries(data, forecast_periods=2)
    assert all(isinstance(v, float) for v in result)


def test_forecast_raises_on_too_few_points():
    with pytest.raises(ValueError):
        forecast_timeseries([1.0, 2.0], forecast_periods=3)


def test_forecast_single_period():
    data = [5.0, 10.0, 15.0, 20.0, 25.0]
    result = forecast_timeseries(data, forecast_periods=1)
    assert len(result) == 1
