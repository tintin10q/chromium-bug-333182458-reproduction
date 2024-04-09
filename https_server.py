
import http.server
import ssl

# Pass phrase is "test"
# Add the CA to chrome

port = 8000
ip = 'localhost'

server_address = (ip, port)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
print("The passphrase is `test`")
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="CA.pem",
                               keyfile="KEY.pem",
                               ssl_version=ssl.PROTOCOL_TLS)
print(f"Started server on {ip}:{port}")
httpd.serve_forever()