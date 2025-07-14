from fastapi import FastAPI
from db.database import engine, Base
from app.api import items, recommendation, sentiment, timeseries, clustering


Base.metadata.create_all(bind=engine)

app = FastAPI(title="ML Platform API")

app.include_router(
    items.router,
    prefix="/items",
    tags=["Items"],
)
app.include_router(
    recommendation.router,
    prefix="/recommendation",
    tags=["Recommendation"],
)
app.include_router(
    sentiment.router,
    prefix="/sentiment",
    tags=["Sentiment"],
)
app.include_router(
    timeseries.router,
    prefix="/timeseries",
    tags=["Timeseries"],
)
app.include_router(
    clustering.router,
    prefix="/clustering",
    tags=["Clustering"],
)
