import http.server
import socketserver

# GET / HTTP/1.1

PORT = 1111


class handler_manual (http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("REQUEST: ", self.requestline)
        if self.path == "/" or self.path == "":
            self.path = "/index.html"  
        if not self.path.startswith("/"):
            self.path = "/" + self.path

        if self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/page2.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("page2.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/page3.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("page3.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        print("REQUEST: ", self.requestline)
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b'hola mundo POST\n')

socketserver.TCPServer.allow_reuse_address = True

myhttphandler = handler_manual

httpd = http.server.HTTPServer(("", PORT), myhttphandler)

print(f"Opening httpd server at port {PORT}")

httpd.serve_forever()

httpd.shutdown()