#!/usr/bin/env python3
"""
Obsidian Aurora — Digital Lab Profile Local Host Server
Serves README.md, SETUP.md, and Obsidian Aurora assets with live browser preview.
"""
import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 3000

class LabHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and disable aggressive caching for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.svg'):
            return 'image/svg+xml'
        if path.endswith('.md'):
            return 'text/plain; charset=utf-8'
        if path.endswith('.js'):
            return 'application/javascript; charset=utf-8'
        if path.endswith('.html'):
            return 'text/html; charset=utf-8'
        return super().guess_type(path)

def run(port=DEFAULT_PORT):
    # Set directory to project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Try requested port or fallback
    selected_port = port
    for p in [port, 8080, 8000, 5000]:
        try:
            with socketserver.TCPServer(("0.0.0.0", p), LabHTTPRequestHandler) as httpd:
                print(f"============================================================")
                print(f"  ◈ OBSIDIAN AURORA — DIGITAL LAB LOCAL HOST SERVER")
                print(f"  ◈ Serving: {script_dir}")
                print(f"  ◈ Localhost URL: http://localhost:{p}")
                print(f"  ◈ Network URL:   http://127.0.0.1:{p}")
                print(f"============================================================")
                sys.stdout.flush()
                httpd.serve_forever()
                break
        except OSError as e:
            if p == 5000:
                print(f"Error starting server: {e}")
                sys.exit(1)
            continue

if __name__ == '__main__':
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run(port)
