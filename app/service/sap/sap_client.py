import requests
from app.config import get_settings
settings = get_settings()

class SAPClient:
    def __init__(self):
        self.base_url = (
            settings.sap_base_url
        )
        self.endpoint = (
            settings.sap_supplier_invoice_endpoint
        )
        self.api_key = (
            settings.sap_api_key
        )
        self.url = (
            f"{self.base_url}"
            f"{self.endpoint}"
        )

    def create_supplier_invoice(
            self,
            payload: dict
    ):
        headers = {
            "Content-Type": "application/json",
            "APIKey": self.api_key
        }

        response = requests.post(
            self.url,
            headers=headers,
            json=payload
        )
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return {
                "status_code": response.status_code,
                "error": response.text
            }
