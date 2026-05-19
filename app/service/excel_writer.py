import pandas as pd
from pathlib import Path


from app.constants import EXCEL_FILE
from app.service.schema.invoice_schema import InvoiceData


class ExcelWriter:

    def __init__(self):

        EXCEL_FILE.parent.mkdir(
            exist_ok=True
        )

    def save_invoice(
            self,
            invoice_data: InvoiceData
    ):
        data = invoice_data.model_dump()

        new_df = pd.DataFrame([data])

        if Path(EXCEL_FILE).exists():

            existing_df = pd.read_excel(EXCEL_FILE)

            updated_df = pd.concat(
                [existing_df, new_df],
                ignore_index=True
            )

        else:
            updated_df = new_df

        updated_df.to_excel(
            EXCEL_FILE,
            index=False
        )