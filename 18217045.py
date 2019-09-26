#!/usr/bin/env python
# coding: utf-8

# In[1]:


import http.server
import socketserver

Pass = "Tesgan"

class handlercuy(http.server.SimpleHTTPRequestHandler):
    def salah(self):
        self.send_response(200)
        self.send_header('salah bro')
        self.send_end
    def benar(self) :
        self.send_response(401)
        self.send_header('hi')
        self.send_end
    def do_GET(self) :
        global key
        if self.headers.get('authorization') == 'Tesgan' :
            self.benar()
        else :trr
            self.salah()t  
        


PORT = 8080
Handler = handlercuy
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# In[1]:


openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem


# In[ ]:


from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

class Handlers(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

httpd = HTTPServer(('localhost', 4443), Handlers)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="key.pem", 
        certfile='certificate.pem', server_side=True)

httpd.serve_forever()


# In[ ]:




