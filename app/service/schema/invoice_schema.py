from pydantic import (
    BaseModel,
    Field
)


class InvoiceData(BaseModel):

    invoice_number: str = Field(...,description="Unique invoice number from invoice")
    vendor_name: str = Field(...,description="Seller or vendor company name")
    grand_total: float = Field(...,description="Final invoice amount including taxes")
    invoice_date: str = Field(...,description="Invoice issue date")
    gstin: str = Field(...,description="GST identification number of vendor")