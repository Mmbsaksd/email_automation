from app.config import get_settings
settings = get_settings()

class EmailFilter:
    def is_allowed_email(self, sender):
        sender = sender.lower()
        allowed_sender = settings.allowed_sender.lower()
        return allowed_sender in sender
    