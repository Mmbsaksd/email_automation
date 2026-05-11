import base64

class EmailParser:
    def parse_header(self, headers):
        email_data = {}

        for header in headers:
            name = header["name"]
            value = header["value"]

            if name == "Subject":
                email_data["subject"] = value

            elif name == "From":
                email_data["from"] = value

            elif name == "Date":
                email_data["date"] = value
        return email_data


    def extract_body(self, payload):
        parts = payload.get("parts",[])

        for part in parts:
            mime_type = part.get("mimeType")
            if mime_type in ["text/plain", "text/html"]:
                data = part["body"].get("data",{})

                if data:
                    decoded_data = base64.urlsafe_b64decode(
                        data
                    ).decode("utf-8")
                    return decoded_data
        return None
