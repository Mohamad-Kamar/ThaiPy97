import http.server

# Create a custom request handler to encapsulate features
class ExampleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle GET requests
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, this is a GET request!')
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'About page')
        else:
            self.send_error(404, 'File Not Found')

    def do_POST(self):
        # Handle POST requests
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'You submitted data: ' + post_data)
        else:
            self.send_error(404, 'File Not Found')

    def do_PUT(self):
        # Handle PUT requests
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'This is a PUT request.')

# Create and start the server
port = 8000
server_address = ('', port)
httpd = http.server.HTTPServer(server_address, ExampleHandler)
print(f"Serving at http://localhost:{port}")
httpd.serve_forever()
