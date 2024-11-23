import csv

def save_to_csv(data):
    """
    Saves the extracted data to a CSV file.
    """
    if isinstance(data, dict):
        with open("extracted_data.csv", "w", newline="") as file:
            fieldnames = ["Tender Reference Number", "Title", "Submission Dates", "Financial Requirements", "Eligibility Criteria", "Technical Specifications", "Contact Information"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
        print("Data saved to extracted_data.csv")
    else:
        print("Data format is not suitable for CSV export.")
