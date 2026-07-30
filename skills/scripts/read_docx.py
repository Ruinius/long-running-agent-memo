import docx
import sys
import os

def read_docx(docx_path, output_stream=sys.stdout):
    if not os.path.exists(docx_path):
        print(f"Error: File not found at '{docx_path}'", file=sys.stderr)
        sys.exit(1)
        
    doc = docx.Document(docx_path)
    
    for block in doc.element.body:
        if block.tag.endswith('p'):
            p = docx.text.paragraph.Paragraph(block, doc)
            style = p.style.name
            text = p.text
            if style.startswith('Heading'):
                output_stream.write(f"\n{text}\n" + "=" * len(text) + "\n")
            elif style.startswith('List'):
                output_stream.write(f"  * {text}\n")
            else:
                output_stream.write(f"{text}\n")
        elif block.tag.endswith('tbl'):
            tbl = docx.table.Table(block, doc)
            output_stream.write("\n[Table]\n")
            for row in tbl.rows:
                cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
                output_stream.write(" | ".join(cells) + "\n")
            output_stream.write("[/Table]\n\n")

if __name__ == "__main__":
    input_path = "output/memo.docx"
    output_path = None
    
    if len(sys.argv) == 2:
        input_path = sys.argv[1]
    elif len(sys.argv) == 3:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
    elif len(sys.argv) > 3:
        print("Usage: python read_docx.py [input.docx] [output.txt]", file=sys.stderr)
        sys.exit(1)
        
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            read_docx(input_path, f)
        print(f"Successfully extracted text to '{output_path}'")
    else:
        read_docx(input_path, sys.stdout)
