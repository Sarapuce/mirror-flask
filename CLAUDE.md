# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`mirror-flask` is a simple HTTP echo/mirror server built with Flask. It accepts any HTTP method on any path and logs all request details (headers, query params, form data, files, IP) to stdout, returning a plain 200 response.

## Running the server

```bash
./start.sh
```

Runs on `0.0.0.0:8875` with debug mode enabled. CORS is open to all origins (`*`).

## Dependencies

- `flask`
- `flask-cors`

Install with:

```bash
pip install flask flask-cors
```

## Slash commands

- `/start` — start the server
- `/kill` — kill the server

## Architecture

The entire application is a single file (`main.py`). A catch-all route handles every path and HTTP method, printing request details to stdout and returning an HTML page (HTTP 200) displaying the request path and headers in a styled table.
