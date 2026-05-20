from datetime import datetime
from app.config import get_settings
from app.service.schema.invoice_schema import InvoiceData
from app.service.schema.sap_invoice_schema import SAPInvoicePayload


settings = get_settings()

class PayloadMapper:
    def map_to_sap_payload(
            self,
            invoice_data: InvoiceData
    ):
        return SAPInvoicePayload(
            CompanyCode=settings.sap_company_code,
            DocumentDate=invoice_data.invoice_date,
            PostingDate=datetime.now().strftime("%Y-%m-%d"),
            SupplierInvoiceIDByInvcgParty=invoice_data.invoice_number,
            DocumentCurrency=settings.sap_currency,
            InvoiceGrossAmount=str(invoice_data.grand_total),
            InvoicingParty=settings.sap_vendor_id
        )