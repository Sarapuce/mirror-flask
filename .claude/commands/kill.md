Your goal is to kill the echo server on port: $ARGUMENTS

The default port is 8875. If the user provides a port argument (e.g. `/kill 9000`), use that port instead.

Do the following:

1. Perform a curl to localhost on the target port to see if the server is alive.
2. If the answer does not correspond to the echo server, stop and do nothing.
3. Else kill the process running the echo server.
4. Wait 1 second, then perform a single curl to verify the server is no longer responding.
   - If it no longer responds, print "Server stopped."
   - If it still responds, print an error message indicating the kill failed.
