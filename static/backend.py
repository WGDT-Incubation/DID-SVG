from flask import Flask, request, send_file, render_template_string, send_from_directory
import cairosvg
import os

app = Flask(__name__, static_folder="static")

TEMPLATE_FILE = 'template.svg'
FILLED_SVG = 'filled_certificate.svg'
PDF_FILE = 'certificate.pdf'

@app.route('/')
def home():
    with open('static/editor.html', 'r', encoding='utf-8') as f:
        html = f.read()
    return render_template_string(html)

@app.route('/form')
def form():
    with open('static/form.html', 'r', encoding='utf-8') as f:
        html = f.read()
    return render_template_string(html)

@app.route('/upload-template', methods=['POST'])
def upload_template():
    svg_data = request.data.decode('utf-8')
    with open(TEMPLATE_FILE, 'w', encoding='utf-8') as f:
        f.write(svg_data)
    return {'status': 'Template saved'}

@app.route('/generate-certificate', methods=['POST'])
def generate_certificate():
    data = request.form if request.form else request.json
    if not os.path.exists(TEMPLATE_FILE):
        return {"error": "Template file not found."}, 404

    # Fill placeholders
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as file:
        svg_content = file.read()
    for key, value in data.items():
        svg_content = svg_content.replace(f"{{{{{key}}}}}", value)
    with open(FILLED_SVG, 'w', encoding='utf-8') as file:
        file.write(svg_content)

    # Convert to PDF
    cairosvg.svg2pdf(url=FILLED_SVG, write_to=PDF_FILE)
    return send_file(PDF_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)