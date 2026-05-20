from app.service.email.gmail_reader import GmailReader
from app.service.email.email_parser import EmailParser
from app.service.email.email_filter import EmailFilter
from app.service.email.attachment_parser import AttachmentParser
from app.service.email.attachment_handler import AttachmentHandler
from app.service.pdf.pdf_reader import PDFReader
from app.service.ai.invoice_extractor import InvoiceExtractor
from app.service.excel_writer import ExcelWriter
from app.service.sap.payload_mapper import PayloadMapper
from app.service.sap.sap_client import SAPClient


parser = EmailParser()
reader = GmailReader()
filter_engine = EmailFilter()
attachment_parser = AttachmentParser()
attachment_handler = AttachmentHandler()
pdf_reader = PDFReader()
invoice_extractor = InvoiceExtractor()
excel_writer = ExcelWriter()
payload_mapper = PayloadMapper()
sap_client = SAPClient()

messages = reader.get_latest_email()

if not messages:
    print("No emails found")
    exit()

message_id = messages[0]["id"]
full_message = reader.get_full_message(message_id)
payload = full_message["payload"]
headers = payload["headers"]
parser_headers = parser.parse_header(headers)



is_allowed = filter_engine.is_allowed_email(
    parser_headers["from"]
)
if not is_allowed:
    print("Blocked Email")
    exit()

body = parser.extract_body(payload)

parser_headers["body"] = body

pdf_attachment = attachment_parser.get_pdf_attachment(
    payload
)
if pdf_attachment:
    attachment_data  = reader.download_attachment(
        message_id,
        pdf_attachment["attachment_id"],
    )
    saved_path = attachment_handler.save_pdf(
        pdf_attachment['filename'],
        attachment_data['data']
    )
    parser_headers["attachment_path"]= str(saved_path)

    pdf_text = pdf_reader.extract_text(saved_path)
    #parser_headers["pdf_text"] = pdf_text
    invoice_data = invoice_extractor.extract_invoice_data(
        pdf_text
    )
    sap_payload = payload_mapper.map_to_sap_payload(invoice_data)
    sap_response = sap_client.create_supplier_invoice(
        sap_payload.model_dump()
    )
    parser_headers["invoice_data"] = invoice_data.model_dump()
    excel_writer.save_invoice(
        invoice_data
    )
else:
    print("No PDF attachment found")
print(parser_headers)
print(sap_response)
