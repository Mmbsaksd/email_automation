from functools import lru_cache

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):

    # Azure OpenAI
    azure_openai_api_key: str
    azure_openai_endpoint: str
    azure_openai_api_version: str

    # Email Sender Filter
    allowed_sender: str = "mmbsaksd@gmail.com"


    sap_api_key: str
    sap_base_url: str
    sap_supplier_invoice_endpoint: str
    sap_company_code: str
    sap_currency: str
    sap_vendor_id: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings():

    return Settings()