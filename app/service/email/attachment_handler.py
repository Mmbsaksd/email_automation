import base64
from pathlib import Path

class AttachmentHandler:
    ATTACHMENT_DIR = Path("attachments")

    def __init__(self):
        self.ATTACHMENT_DIR.mkdir(exist_ok=True)
    
    def save_pdf(
            self,
            filename,
            data
    ):
        file_path = self.ATTACHMENT_DIR / filename
        file_bytes = base64.urlsafe_b64decode(data)
        with open(file_path, "wb") as file:
            file.write(file_bytes)

        return file_path

