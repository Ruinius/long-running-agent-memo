import sys
import markdown
from xhtml2pdf import pisa

def export_to_pdf(markdown_path, pdf_path):
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Sanitize text to replace special unicode characters that render as squares in xhtml2pdf
    md_text = md_text.replace('\u2011', '-') # Non-breaking hyphen
    md_text = md_text.replace('\u2012', '-') # Figure dash
    md_text = md_text.replace('\u2013', '-') # En dash
    md_text = md_text.replace('\u2014', '--') # Em dash
    md_text = md_text.replace('\u2018', "'").replace('\u2019', "'") # Smart single quotes
    md_text = md_text.replace('\u201C', '"').replace('\u201D', '"') # Smart double quotes

    # Convert markdown to html
    html_content = markdown.markdown(md_text, extensions=['extra', 'tables'])

    # Wrap tables in a div to help xhtml2pdf handle page-break-inside: avoid
    import re
    html_content = re.sub(r'(<table>.*?</table>)', r'<div class="table-wrapper">\1</div>', html_content, flags=re.DOTALL)

    html_string = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <style>
            @page {{
                size: letter;
                margin: 1.8cm 1.8cm 1.8cm 1.8cm;
            }}
            body {{
                font-family: Helvetica, Arial, sans-serif;
                line-height: 1.25;
                color: #333;
                font-size: 10pt;
            }}
            h1 {{
                font-size: 16pt;
                color: #2c3e50;
                border-bottom: 1px solid #3498db;
                padding-bottom: 6px;
                margin-top: 15px;
                margin-bottom: 10px;
                font-weight: normal;
            }}
            h2 {{
                font-size: 12pt;
                color: #2c3e50;
                margin-top: 15px;
                margin-bottom: 6px;
                font-weight: bold;
            }}
            h3 {{
                font-size: 10.5pt;
                color: #2c3e50;
                margin-top: 10px;
                margin-bottom: 4px;
                font-weight: bold;
            }}
            blockquote {{
                margin: 6px 0;
                padding: 6px 12px;
                background-color: #f8f9fa;
                border-left: 3px solid #cbd5e1;
                font-style: italic;
                color: #475569;
            }}
            p {{
                margin-bottom: 8px;
                text-align: left;
            }}
            ul {{
                margin-bottom: 8px;
            }}
            li {{
                margin-bottom: 3px;
            }}
            strong {{
                font-weight: bold;
                color: #1a252f;
            }}
            pre {{
                background-color: #f8fafc;
                border: 1px solid #cbd5e1;
                border-radius: 4px;
                padding: 8px;
                font-family: Courier, 'Courier New', monospace;
                font-size: 8pt;
                line-height: 1.25;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
            code {{
                font-family: Courier, 'Courier New', monospace;
                font-size: 8.5pt;
                background-color: #f1f5f9;
                padding: 1px 3px;
            }}
            .table-wrapper {{
                page-break-inside: avoid;
                display: block;
                width: 100%;
            }}
            tr {{
                page-break-inside: avoid;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 8px;
                margin-bottom: 8px;
                font-size: 8.5pt;
                page-break-inside: avoid;
            }}
            th {{
                text-align: left;
                padding: 5px;
                border: 1px solid #cbd5e1;
                font-weight: bold;
                color: #1e293b;
                word-wrap: break-word;
                vertical-align: top;
                background-color: #f1f5f9;
            }}
            td {{
                padding: 5px;
                border: 1px solid #cbd5e1;
                color: #334155;
                word-wrap: break-word;
                vertical-align: top;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    with open(pdf_path, "wb") as result_file:
        pisa_status = pisa.CreatePDF(html_string, dest=result_file)

    if pisa_status.err:
        print(f"Error creating PDF: {pisa_status.err}")
        sys.exit(1)
    else:
        print(f"Successfully created {pdf_path}")

if __name__ == "__main__":
    import os
    if len(sys.argv) == 1:
        input_path = "output/memo.md"
        output_path = "output/memo.pdf"
    elif len(sys.argv) == 2:
        input_path = sys.argv[1]
        base, _ = os.path.splitext(input_path)
        output_path = base + ".pdf"
    elif len(sys.argv) == 3:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
    else:
        print("Usage: python export_pdf.py [input.md] [output.pdf]")
        sys.exit(1)
    
    export_to_pdf(input_path, output_path)
