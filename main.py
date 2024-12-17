from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def catch_all(path):
    print(f"Path: {path}")
    print(f"Method: {request.method}")
    print("Headers:")
    for header, value in request.headers.items():
        print(f"  {header}: {value}")
    print("Parameters:")
    for param, value in request.args.items():
        print(f"  {param}: {value}")
    print("Form Data:")
    for key, value in request.form.items():
        print(f"  {key}: {value}")
    print(f"IP : {request.remote_addr}")
    if 'file' in request.files:
        uploaded_file = request.files['file']
        print("File received:")
        print(f"  Filename: {uploaded_file.filename}")
        print("  Content:")
        print(uploaded_file.read())
    return "Request received and logged.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8875, debug=True)
