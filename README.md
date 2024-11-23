## Cleaned-up README.md with Improved Formatting and Readability

**Document Processing with Streamlit**

This project processes a PDF document, extracts relevant information using language models, and displays the extracted data in a user-friendly Streamlit web app. It leverages a combination of techniques:

* Text extraction from PDF documents, removing dynamic headers.
* Optical Character Recognition (OCR) for image-based PDFs with Tesseract OCR.
* Retrieval-Augmented Generation (RAG) model for targeted field extraction.
* FAISS vectorstore for efficient information retrieval.

## Features

- **PDF Text Extraction:** Extracts text from PDF documents and removes dynamic headers.
- **OCR Processing:** Leverages Tesseract OCR to extract text from image-based PDFs.
- **Information Extraction:** Employs a language model to extract specific fields (e.g., Tender Reference Number, Title, Dates).
- **FAISS Vectorstore:** Implements efficient information extraction through FAISS-based similarity search.

## Prerequisites

**Ensure you have the following installed:**

* Python 3.8+
* Tesseract OCR (for OCR processing)
* Ollama CLI (for interacting with language models)

**Tesseract OCR Installation:**

1. Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
2. Configure the Tesseract path in your environment variables, or set it in the code (`pytesseract.pytesseract.tesseract_cmd`).

**Ollama CLI Installation:**

- Ollama CLI is required to interact with the language models. Follow the instructions based on your OS:

   **Windows:**

   1. Download the Ollama installer: [Ollama installer for Windows](https://ollama.com/download).
   2. Run the installer and follow the prompts.

   **macOS:**

   ```bash
   brew install ollama
   ```

   **Linux:**

   Follow the installation guide: [Linux installation guide](https://ollama.com/docs/get-started)

**Verification:**

After installation, verify with:

```bash
ollama --version
```

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <project_folder>
   ```

2. **Install dependencies (Python 3.8+ required):**

   ```bash
   pip install -r requirements.txt
   ```

## Running the App

**Option 1: Using the `run_app.bat` File (Windows Users Only)**

For convenience, a batch file (`run_app.bat`) automatically installs dependencies and starts the Streamlit app. Double-click it.

**Option 2: Manual Setup (Without `.bat` File)**

1. **Install dependencies:**

   Open a terminal or command prompt, navigate to the project folder, and run:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

The Streamlit app should open in your web browser.

## Troubleshooting

1. **Missing Dependencies:**

   - Ensure all required packages are listed in `requirements.txt`. Run `pip freeze` to check installed packages and versions.

2. **Tesseract Not Found:**

   - Verify Tesseract installation and path configuration in the code (`pytesseract.pytesseract.tesseract_cmd`).

3. **Ollama CLI Not Found:**

   - Verify Ollama CLI installation and its presence in your system's PATH. Check with `ollama --version`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
