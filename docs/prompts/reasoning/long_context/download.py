import requests
import fitz  # PyMuPDF
from io import BytesIO

def download_and_extract_pdf(url, output_file):
    """
    Download a PDF from a URL and extract all text to a file.
    
    Args:
        url: URL of the PDF to download
        output_file: Path to the output text file
    """
    print(f"Downloading PDF from {url}...")
    response = requests.get(url)
    response.raise_for_status()
    
    print("Extracting text from PDF...")
    pdf_file = BytesIO(response.content)
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    
    text = ''
    for page_num, page in enumerate(doc, 1):
        print(f"Processing page {page_num}/{len(doc)}...")
        text += page.get_text()
        text += '\n\n'  # Add spacing between pages
    
    doc.close()
    
    print(f"Writing text to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Done! Extracted {len(text)} characters from {len(doc)} pages.")

if __name__ == "__main__":
    url = "https://www.txs.uscourts.gov/sites/txs/files/newby6028.pdf"
    output_file = "newby6028.txt"
    
    download_and_extract_pdf(url, output_file)
