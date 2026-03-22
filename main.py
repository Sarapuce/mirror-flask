import argparse
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
    headers_rows = "".join(f"<tr><td><b>{h}</b></td><td>{v}</td></tr>" for h, v in request.headers.items())
    response_body = f"""<!DOCTYPE html>
<html>
<head><style>
  body {{ font-family: monospace; padding: 2em; }}
  h2 {{ border-bottom: 2px solid black; padding-bottom: 4px; }}
  table {{ border-collapse: collapse; width: 100%; }}
  td {{ padding: 4px 12px; vertical-align: top; }}
  tr:nth-child(even) {{ background: #f2f2f2; }}
</style></head>
<body>
  <h2>PATH</h2>
  <p>/{path}</p>
  <h2>HEADERS</h2>
  <table>{headers_rows}</table>
</body>
</html>"""
    return response_body, 200

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8875)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=True)
