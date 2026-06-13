import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def analyze_csv(file_path: str, question: str) -> dict:
    """Analyze a CSV file and answer a question about it.
    Args:
        file_path: Path to the CSV file.
        question: The analytical question to answer.
    Returns: Dict with the analysis result.
    """
    import pandas as pd

    # If the path is not absolute, resolve it relative to this package's directory
    if not os.path.isabs(file_path):
        file_path = os.path.join(BASE_DIR, file_path)

    df = pd.read_csv(file_path)
    summary = {"rows": len(df), "columns": list(df.columns)}
    # Add category revenue breakdown if applicable
    if "revenue" in df.columns and "category" in df.columns:
        summary["revenue_by_category"] = df.groupby("category")["revenue"].sum().sort_values(ascending=False).to_dict()
    return summary


def calculate_metrics(data: list, metric: str) -> dict:
    """Calculate statistical metrics on a list of numbers.
    Args
        data: List of numeric values to analyze.
        metric: One of "mean", "median", "sum", "growth".
    Returns: Dict with the computed metric value.
    """
    import statistics
    result = getattr(statistics, metric)(data)
    return {"metric": metric, "value": result}