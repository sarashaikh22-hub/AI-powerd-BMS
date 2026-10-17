
import pandas as pd


def load_processed_csv(file_path):
    """Load a processed battery dataset in CSV format."""
    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("The processed dataset is empty.")

    return df


def validate_columns(df, required_columns):
    """Check whether required fields are present."""
    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(missing)}"
        )

    return True
