def extract_information_with_similarity_search(vectorstore, llm, prompt, texts):
    """
    Extracts specific fields from the document using similarity search and LLM prompts.
    """
    extracted_fields = {
        "Tender Reference Number": "",
        "Title": "",
        "Submission Dates": "",
        "Financial Requirements": "",
        "Eligibility Criteria": "",
        "Technical Specifications": "",
        "Contact Information": ""
    }

    for field in extracted_fields.keys():
        field_prompt = prompt.replace("{extracted_text}", f"What is the **{field}**?")
        response = llm.invoke(field_prompt)

        # Assign the response to the appropriate field
        extracted_fields[field] = response.content.strip()

    return extracted_fields
