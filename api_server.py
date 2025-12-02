from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        # 告诉浏览器返回的是JSON数据
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # 要返回的数据（服务名称、状态、版本）
        response = {"status": "active", "service": "OrderService", "version": "1.0"}
        self.wfile.write(json.dumps(response).encode())

# 让服务在8080端口运行（所有IP都能访问）
server_address = ('', 8080)
print("Microservice starting on port 8080...")
httpd = HTTPServer(server_address, SimpleAPI)
httpd.serve_forever()
