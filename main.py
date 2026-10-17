
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Predictive Battery Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Predictive BMS API is running"
    }


@app.get("/api/dashboard")
def dashboard(
    battery: str = Query(
        default="B0005",
        pattern="^B0005$|^B0006$|^B0007$|^B0018$"
    )
):
    return {
        "battery_id": battery,
        "health": None,
        "remaining_useful_life": None,
        "anomaly_status": "Pending",
        "data_status": "Dataset integration pending",
        "message": (
            "API connected. Processed NASA data and a validated "
            "prediction model are not connected yet."
        )
    }
