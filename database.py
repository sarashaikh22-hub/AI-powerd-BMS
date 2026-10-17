
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "battery_data.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS battery_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                battery_id TEXT NOT NULL,
                cycle INTEGER,
                capacity REAL,
                voltage REAL,
                temperature REAL
            )
        """)


if __name__ == "__main__":
    initialize_database()
    print(f"Database initialized: {DB_PATH}")
