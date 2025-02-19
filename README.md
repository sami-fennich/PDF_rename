# PDF Auto-Renamer

A Python script that automatically renames PDF files based on their content. The script extracts meaningful text from the first page of each PDF and uses it to generate a new filename.

## Features

- Automatically processes all PDF files in the script's directory
- Extracts text from the first page of each PDF
- Creates filenames using the first 5 meaningful words from the content
- Handles duplicate filenames by adding incremental numbers
- Removes special characters from filenames
- Provides console output for tracking the renaming process

## Requirements

- Python 3.x
- PyMuPDF (fitz) library

To install the required library:
```bash
pip install PyMuPDF
```

## Usage

1. Place the script in the directory containing your PDF files
2. Run the script:
```bash
python rename_pdfs.py
```

## How It Works

### Main Functions

#### `extract_meaningful_text(pdf_path, num_words=5)`
- Takes a PDF file path and optional number of words as parameters
- Opens the PDF and extracts text from the first page
- Filters out non-alphanumeric words
- Returns the first `num_words` joined with underscores
- Returns `None` if no meaningful text is found or in case of errors

#### `rename_pdfs_in_directory()`
- Scans the current directory for PDF files
- Processes each PDF using `extract_meaningful_text()`
- Generates new filenames based on the extracted text
- Handles filename conflicts by adding numbers
- Renames files and prints status messages

## Output Format

New filenames will be in the format:
- `word1_word2_word3_word4_word5.pdf`
- If duplicate: `word1_word2_word3_word4_word5_1.pdf`

## Error Handling

The script includes error handling for:
- PDF reading errors
- File access issues
- Duplicate filenames
- Invalid characters in filenames

## Example

Original filename:
```
document123.pdf
```

After running the script (assuming the PDF contains "Quarterly Financial Report 2024"):
```
Quarterly_Financial_Report_2024.pdf
```

## Notes

- The script only processes files with `.pdf` extension (case-insensitive)
- Only text from the first page is considered
- Special characters are removed from the new filename
- The original file extension (.pdf) is preserved
- The script must have write permissions in the directory

## Limitations

- Only processes PDFs in the same directory as the script
- Requires PDFs to have readable text (not scanned images)
- Limited to the first page content
- Maximum of 5 words in the new filename by default

## Contributing

Feel free to submit issues and enhancement requests.
