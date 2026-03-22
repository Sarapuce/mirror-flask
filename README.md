# mirror-flask

A simple HTTP echo/mirror server built with Flask. Accepts any HTTP method on any path, logs all request details (headers, query params, form data, files, IP) to stdout, and returns an HTML page displaying the request path and headers.

## Usage

```bash
./start.sh [--port <port>]
```

Default port is `8875`. Example with a custom port:

```bash
./start.sh --port 9000
```

## Dependencies

- `flask`
- `flask-cors`

```bash
pip install flask flask-cors
```
