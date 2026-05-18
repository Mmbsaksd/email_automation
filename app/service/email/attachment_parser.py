class AttachmentParser:
    def get_pdf_attachment(self, payload):
        if "parts" in payload:
            for part in payload["parts"]:
                result = self.get_pdf_attachment(part)
                if result:
                    return result
                
        filename = payload.get("filename")
        mime_type = payload.get("mimeType")
        if mime_type == "application/pdf":
            attachment_id = payload.get(
                "body",
                {}
            ).get("attachmentId")

            return {
                "filename": filename,
                "attachment_id": attachment_id
            }
        return None