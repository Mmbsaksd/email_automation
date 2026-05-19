from langchain_openai import AzureChatOpenAI
from app.config import get_settings
from app.service.schema.invoice_schema import InvoiceData
settings = get_settings()

class InvoiceExtractor:
    def __init__(self):
        llm = AzureChatOpenAI(
            api_key=settings.azure_openai_api_key,
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version,
            deployment_name="gpt-4o-mini",
            temperature=0
        )
        self.llm = llm.with_structured_output(InvoiceData)
    
    def extract_invoice_data(
            self,
            pdf_text
    ):
        prompt = f"""
        Extract invoice information from this invoice text.

        Invoice Text:
        {pdf_text}
        """

        response = self.llm.invoke(prompt)
        return response