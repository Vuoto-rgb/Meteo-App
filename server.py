
import http.server
import socketserver
import webbrowser
import os
from pathlib import Path


PORT = 8001
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
       
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
   
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"Weather Dress Advisor Web GUI")
            print(f"=" * 40)
            print(f"Server running at: http://localhost:{PORT}")
            print(f"Serving files from: {DIRECTORY}")
            print(f"=" * 40)
            print(f"Press Ctrl+C to stop the server")
            print(f"=" * 40)
            
          
            webbrowser.open(f'http://localhost:{PORT}')
            
           
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\nServer stopped. Goodbye!")
    except OSError as e:
        if e.errno == 48:  
            print(f"Port {PORT} is already in use. Please try a different port.")
        else:
            print(f"Error starting server: {e}")

if __name__ == "__main__":
    start_server()
