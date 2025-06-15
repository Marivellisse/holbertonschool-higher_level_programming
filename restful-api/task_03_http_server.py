#!/usr/bin/env python3
"""
Task 3: Develop a simple API using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for a simple API.
    """

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode())


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """
    Start the server on localhost at port 8000.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on http://localhost:8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
