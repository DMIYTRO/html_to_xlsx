from flask import Flask, render_template, request, send_file
from html2excel import ExcelParser
import os

app = Flask(__name__)


@app.route('/')
def ui():
    return render_template("ui.html")


@app.route('/api/v1/to_excel', methods=['POST'])
def post():
    save_dir = "./tmp"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    res = request.files.get('input')
    file_path = os.path.join(save_dir, 'convert.html')
    if res is None:
        return "No file selected"
    res.save(file_path)
    parser = ExcelParser(file_path)
    save_path = os.path.join(save_dir, "converted.xlsx")
    parser.to_excel(save_path)
    return send_file(save_path)




if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')
