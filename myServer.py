from http.server import HTTPServer, BaseHTTPRequestHandler


HOST = "127.0.0.1"
PORT = 8008

def returnHTML():
    return """<html>
    <body>
        <h1>Hello Server</h1>
    </body>
</html>"""

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(returnHTML(), "utf-8"))


server = HTTPServer((HOST, PORT), Server)
print(f"Server running at https://{HOST}/{PORT}")
server.serve_forever()
