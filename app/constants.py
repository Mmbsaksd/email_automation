from pathlib import Path

BASE_DIR: str = Path(__file__).resolve().parent.parent.parent
DATA_DIR: str = BASE_DIR / "data"
EXCEL_FILE: str = DATA_DIR / "invoices.xlsx"