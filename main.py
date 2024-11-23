import os
from extract_text import extract_text_with_dynamic_header_removal
from preprocess import preprocess_document
from vectorstore import create_vectorstore
from extraction import extract_information_with_similarity_search
from save_to_csv import save_to_csv
from langchain_ollama import ChatOllama

# Configure LLM Model
MODEL_NAME = "llama3.2"
llm = ChatOllama(model=MODEL_NAME, temperature=0)

PROMPT = """
You are an AI designed to extract specific information from documents. For each of the following fields, I want you to search the document and respond with only the relevant information. If any field is missing or unclear, leave it blank.

Please answer each question below separately and provide only the relevant data for that field.

what is {field} ?

Now, please answer each of the questions based on the following text:

{extracted_text}
"""

def main(input_file):
    print("Extracting text from PDF with dynamic header removal...")
    raw_text = extract_text_with_dynamic_header_removal(input_file)

    if len(raw_text.strip()) == 0:
        print("No meaningful text extracted from the document.")
        return

    print("Preprocessing the document...")
    chunks = preprocess_document(raw_text)

    print("Creating FAISS vectorstore...")
    vectorstore, texts = create_vectorstore(chunks)  # Store the texts separately

    print("Extracting information...")
    extracted_data = extract_information_with_similarity_search(vectorstore, llm, PROMPT, texts)
    print(extracted_data)

    # Save the extracted data to CSV
    save_to_csv(extracted_data)

if __name__ == "__main__":
    INPUT_FILE = "document.pdf"  # Replace with the actual file name
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"Input file '{INPUT_FILE}' not found.")

    main(INPUT_FILE)
