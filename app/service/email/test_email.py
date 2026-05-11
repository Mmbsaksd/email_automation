from app.service.email.gmail_reader import GmailReader
reader = GmailReader()

email = reader.get_latest_email()
print(email)