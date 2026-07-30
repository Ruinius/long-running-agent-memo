import pypdf
import sys
import os

def read_pdf(pdf_path, output_stream=sys.stdout):
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at '{pdf_path}'", file=sys.stderr)
        sys.exit(1)
        
    reader = pypdf.PdfReader(pdf_path)
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        output_stream.write(f"--- Page {i + 1} ---\n")
        output_stream.write(text)
        output_stream.write("\n")

if __name__ == "__main__":
    input_path = "output/memo.pdf"
    output_path = None
    
    if len(sys.argv) == 2:
        input_path = sys.argv[1]
    elif len(sys.argv) == 3:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
    elif len(sys.argv) > 3:
        print("Usage: python read_pdf.py [input.pdf] [output.txt]", file=sys.stderr)
        sys.exit(1)
        
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            read_pdf(input_path, f)
        print(f"Successfully extracted text to '{output_path}'")
    else:
        read_pdf(input_path, sys.stdout)
