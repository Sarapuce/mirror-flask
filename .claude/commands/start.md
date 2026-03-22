Your goal is to start the echo server on port: $ARGUMENTS

The default port is 8875. If the user provides a port argument (e.g. `/start --port 9000`), use that port instead.

Do the following:

1. Check if the server is already running by curling localhost on the target port.
   - If it responds like the echo server (returns PATH and HEADERS), inform the user it is already running and stop.

2. Try to run "./start.sh [--port <port>]" in the background, passing the port argument if provided.

3. Handle errors:
   - If the output contains dependency/import errors (e.g. ModuleNotFoundError), install the missing packages with pip and retry.
   - If the port is already in use by another process, inform the user and stop.
   - For any other error, show the error output to the user and stop.

4. Wait 1 second, then perform a single curl to localhost on the target port to check if the server is responding.

5. Once alive, print the server URL clearly: "Server is running at http://localhost:<port>"
