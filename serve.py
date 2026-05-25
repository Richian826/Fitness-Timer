"""组间计时 — 本地测试服务器
Usage: python serve.py
然后手机连同一WiFi，访问 http://<本机IP>:8080
"""
import http.server
import socket, os

PORT = 8080
os.chdir(os.path.dirname(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        # GitHub Pages 不设 Service-Worker-Allowed，本地免除限制:
        self.send_header("Service-Worker-Allowed", "/")
        super().end_headers()

server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
local_ip = socket.gethostbyname(socket.gethostname())
print(f"服务器已启动: http://{local_ip}:{PORT}")
print("手机上打开此地址即可测试。Ctrl+C 停止。")
server.serve_forever()
