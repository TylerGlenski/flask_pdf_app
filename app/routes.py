from flask import Flask, render_template, make_response
from app import app
import pdfkit

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/generate_pdf')
def generate_pdf():
    rendered = render_template('index.html')
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

    return response