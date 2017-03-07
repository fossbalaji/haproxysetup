import BaseHTTPServer


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        s.wfile.write("Hello From Server 2")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('127.0.0.1', 8002),MyHandler)
    httpd.serve_forever()