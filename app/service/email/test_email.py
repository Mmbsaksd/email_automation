from app.service.email.gmail_reader import GmailReader
from app.service.email.email_parser import EmailParser

parser = EmailParser()
reader = GmailReader()

messages = reader.get_latest_email()

message_id = messages[0]["id"]

full_message = reader.get_full_message(message_id)

payload = full_message["payload"]

headers = payload["headers"]

parser_headers = parser.parse_header(headers)

body = parser.extract_body(payload)

parser_headers["body"] = body

#print(payload)
print(parser_headers)