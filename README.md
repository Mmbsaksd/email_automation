# Email Automation

This application reads the latest Gmail message, checks whether the sender is allowed, downloads a PDF invoice attachment, extracts invoice data with Azure OpenAI, and saves the result to an Excel file.

## What The App Does

- Connects to Gmail using OAuth credentials.
- Reads the latest email from the authenticated Gmail account.
- Allows processing only when the sender matches `ALLOWED_SENDER`.
- Finds and downloads a PDF attachment.
- Extracts text from the PDF.
- Uses Azure OpenAI to extract invoice fields.
- Saves invoice data to `data/invoices.xlsx`.
- Includes SAP supplier invoice client code, but SAP posting is currently commented out in the email test flow.

## Project Structure

```text
app/
  main.py                         Sample Excel writer smoke test
  config.py                       Environment configuration
  service/
    email/
      test_email.py               Main email invoice processing script
      gmail_reader.py             Gmail authentication and message access
      email_filter.py             Allowed sender check
      attachment_parser.py        PDF attachment detection
      attachment_handler.py       PDF attachment saving
      email_parser.py             Email header/body parsing
    pdf/
      pdf_reader.py               PDF text extraction
    ai/
      invoice_extractor.py        Azure OpenAI invoice extraction
    excel_writer.py               Writes invoice rows to Excel
    sap/
      sap_client.py               SAP API client
data/
  invoices.xlsx                   Generated invoice output
attachments/
  *.pdf                           Downloaded email attachments
credentials.json                  Google OAuth client credentials
token.json                        Generated Gmail OAuth token
.env                              Local app configuration
requirements.txt                  Python dependencies
```

## Requirements

- Python 3.12 or newer is recommended.
- A Gmail account.
- Google OAuth desktop credentials saved as `credentials.json`.
- Azure OpenAI credentials.
- SAP API credentials if you plan to enable SAP posting.

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root with these values:

```env
AZURE_OPENAI_API_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_OPENAI_API_VERSION=2025-01-01-preview

ALLOWED_SENDER=sender@example.com

SAP_API_KEY=your_sap_api_key
SAP_BASE_URL=https://sandbox.api.sap.com
SAP_SUPPLIER_INVOICE_ENDPOINT=/s4hanacloud/sap/opu/odata/sap/API_SUPPLIERINVOICE_PROCESS_SRV/A_SupplierInvoice
SAP_COMPANY_CODE=1000
SAP_CURRENCY=INR
SAP_VENDOR_ID=VENDOR_001
```

Do not commit real secrets to Git.

## Gmail OAuth Setup

1. Create a Google Cloud project.
2. Enable the Gmail API.
3. Create OAuth client credentials for a desktop application.
4. Download the credentials file.
5. Save it in the project root as:

```text
credentials.json
```

The first time the app runs, it opens a browser for Google login and creates:

```text
token.json
```

That token is reused on later runs.

## How To Run

From the project root, activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run the main email invoice processing script:

```powershell
python -m app.service.email.test_email
```

The script processes the latest Gmail message only.

## Output

When a valid email with a PDF invoice is found:

- The PDF is saved under `attachments/`.
- Extracted invoice data is appended to `data/invoices.xlsx`.
- Parsed email and invoice data are printed in the terminal.

The extracted invoice fields are:

- `invoice_number`
- `vendor_name`
- `grand_total`
- `invoice_date`
- `gstin`

## Smoke Test

To test only Excel writing:

```powershell
python -m app.main
```

This writes sample invoice data to `data/invoices.xlsx`.

## Troubleshooting

### `google.auth.exceptions.RefreshError: invalid_grant`

This usually means `token.json` is expired, revoked, or no longer valid for the current Google OAuth credentials.

Rename or remove `token.json`, then run the app again:

```powershell
Rename-Item token.json token.old.json
python -m app.service.email.test_email
```

Google login should run again and generate a fresh token.

### `No module named app.test_email`

Use the full module path. The file is not located directly under `app/`.

Correct command:

```powershell
python -m app.service.email.test_email
```

Incorrect command:

```powershell
python -m app.test_email
```

### `Blocked Email`

The sender of the latest email does not match `ALLOWED_SENDER` in `.env`.

Update `ALLOWED_SENDER` or test with an email from the allowed sender.

### `No PDF attachment found`

The latest email does not contain a PDF attachment. Send or select an email with a PDF invoice attached.

## Notes

- The app currently reads only the latest Gmail message.
- SAP posting code exists in `app/service/sap/`, but the call is commented out in `app/service/email/test_email.py`.
- Keep `credentials.json`, `token.json`, and `.env` private because they contain sensitive authentication data.
