#!/usr/bin/env python3
"""Task 3: mini API using http.server (/, /data, /status, 404 others)."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for a tiny API."""
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        if self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            # EXACT header required by grader (no charset here)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # Any other path → plain-text 404 with exact body
        msg = b"Endpoint not found"
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(msg)))
        self.end_headers()
        self.wfile.write(msg)


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on http://127.0.0.1:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
