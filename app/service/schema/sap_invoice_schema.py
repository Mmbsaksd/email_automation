from pydantic import BaseModel, Field


class SAPInvoicePayload(BaseModel):
     CompanyCode: str = Field(..., description="SAP company code")
     DocumentDate: str = Field(..., description="Invoice date")
     PostingDate: str = Field(..., description="SAP posting date")
     SupplierInvoiceIDByInvcgParty: str = Field(..., description="Vendor invoice number")
     DocumentCurrency: str = Field(..., description="Invoice currency")
     InvoiceGrossAmount: str = Field(..., description="Total invoice amount")
     InvoicingParty: str = Field(..., description="Vendor ID in SAP")