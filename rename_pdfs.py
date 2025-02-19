import os
import fitz  # PyMuPDF
import re

def extract_meaningful_text(pdf_path, num_words=5):
    """Extracts the first meaningful text from the first page of a PDF."""
    try:
        doc = fitz.open(pdf_path)
        text = doc[0].get_text("text")  # Extract raw text from the first page
        doc.close()
        
        # Clean and extract meaningful words
        words = [word for word in re.findall(r"\b[A-Za-z]{5,}\b", text)]
        if words:
            return "_".join(words[:num_words])
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
    
    return None

def rename_pdfs_in_directory():
    """Renames all PDF files in the same directory as the script based on content."""
    directory = os.getcwd()
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith(".pdf")]
    
    for pdf in pdf_files:
        old_path = os.path.join(directory, pdf)
        new_name = extract_meaningful_text(old_path)
        
        if new_name:
            new_name = re.sub(r'[^A-Za-z0-9_-]', '', new_name)  # Remove special characters
            new_path = os.path.join(directory, f"{new_name}.pdf")
            
            counter = 1
            while os.path.exists(new_path):
                new_path = os.path.join(directory, f"{new_name}_{counter}.pdf")
                counter += 1
            
            os.rename(old_path, new_path)
            print(f"Renamed: {pdf} -> {os.path.basename(new_path)}")
        else:
            print(f"Skipping: {pdf} (no meaningful text found)")

if __name__ == "__main__":
    rename_pdfs_in_directory()
