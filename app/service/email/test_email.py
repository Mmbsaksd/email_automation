from app.service.email.gmail_reader import GmailReader
from app.service.email.email_parser import EmailParser
from app.service.email.email_filter import EmailFilter

parser = EmailParser()
reader = GmailReader()
filter = EmailFilter()

messages = reader.get_latest_email()

message_id = messages[0]["id"]

full_message = reader.get_full_message(message_id)

payload = full_message["payload"]

headers = payload["headers"]

parser_headers = parser.parse_header(headers)



is_allowed = filter.is_allowed_email(
    parser_headers["from"]
)
if not is_allowed:
    print("Blocked Email")
    exit()

body = parser.extract_body(payload)

parser_headers["body"] = body

#print(payload)
print(parser_headers)