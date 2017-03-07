import BaseHTTPServer


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        s.wfile.write("Hello From Server 1")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('localhost', 8001),MyHandler)
    httpd.serve_forever()