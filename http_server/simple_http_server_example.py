import http.server
import socketserver

# Specify the IP address and port to listen on
host = '0.0.0.0'  # Listen on all available network interfaces
port = 8000

# Create a custom request handler to display additional features
class ExampleServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Display the client's IP address
        client_ip = self.client_address[0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'Client IP: {client_ip}\n'.encode('utf-8'))

with socketserver.TCPServer((host, port), ExampleServer) as httpd:
    print(f"Serving at http://{host}:{port}")
    httpd.serve_forever()
