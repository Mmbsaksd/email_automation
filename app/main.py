from app.service.excel_writer import ExcelWriter

invoice_data = {
    "vendor_name": "ABC Pvt Ltd",
    "invoice_number": "INV-1001",
    "price": 25000,
    "currency": "INR"
}

writer = ExcelWriter()
writer.save_invoice(invoice_data)
print("Invoice saved successfully")