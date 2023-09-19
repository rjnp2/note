# certificate_app/views.py
from cairosvg import svg2pdf

svg_path = 'certificate_svg/certificate_skeleton.svg'
def generate_certificate(full_name, certificate_id, completed_date):
    # Load the SVG template and replace the placeholder with the full name    
    with open(svg_path, 'r') as svg_file:
        svg_template = svg_file.read()
        svg_template = svg_template.replace('{{ full_name }}', full_name)
        svg_template = svg_template.replace('{{ certificate_id }}', certificate_id)
        svg_template = svg_template.replace('{{ completed_date }}', completed_date)
    
    # Convert the SVG template to a PDF
    pdf_data = svg2pdf(bytestring=svg_template.encode('utf-8'))

     # Define the path where the PDF will be saved temporarily
    temp_pdf_path = 'temp.pdf'
    
    # Save the PDF temporarily
    with open(temp_pdf_path, 'wb') as pdf_file:
        pdf_file.write(pdf_data)
    
    return pdf_file
    
