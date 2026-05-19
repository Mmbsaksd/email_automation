import fitz

class PDFReader:
    def extract_text(
            self,
            pdf_path
    ):
        document = fitz.open(pdf_path)
        full_text = ""
        for page in document:
            text = page.get_text()
            full_text +=text
        document.close()

        return full_text