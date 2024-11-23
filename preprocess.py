from langchain.text_splitter import CharacterTextSplitter

def preprocess_document(text):
    """
    Preprocesses the extracted text by splitting it into chunks of size 500 with an overlap of 50 characters.
    """
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    return chunks
