"""
    Custom Python Web Server Gateway Interface
"""

import io
import socket
import sys
import datetime
import pytz

class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 10                                                         # Client queue size

    def __init__(self, server_address):
        self.listen_socket = listen_socket = socket.socket(                         # Listening socket
            self.address_family,
            self.socket_type
        )

        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         # Allow address reuse
        listen_socket.bind(server_address)                                          # Bind
        listen_socket.listen(self.request_queue_size)                               # Activate
        host, port = self.listen_socket.getsockname()[:2]                           # Get server host name and port:
        self.server_name = socket.getfqdn(host)                                     # - hostname
        self.server_port = port                                                     # - port
        self.headers_set = []                                                       # Return header ser by Web framework/Web application

    def set_app(self, application):
        self.application = application
    
    def serve_forever(self):
        listen_socket = self.listen_socket

        while True:
            self.client_connection, client_address = listen_socket.accept()         # New client connection
            """
                Handle one request and close the client connection. Then
                loop over to wait fo another client connection, this only
                handles 1 client per request.
            """
            self.handle_one_request()
    
    def handle_one_request(self):
        request_data = self.client_connection.recv(1024)
        self.request_data = request_data = request_data.decode("utf-8")

        print("".join(f"< {line}\n" for line in request_data.splitlines()))          # Print formatted request data a la 'curl -v
        
        self.parse_request(request_data)
        env = self.get_environ()                                                     # Construct environment dict using request data
        """
            Call application and return a result of an HTTP response
            body.
        """
        result = self.application(env, self.start_response)
        self.finish_response(result)                                                 # Construct a response and send it back to client
    
    def parse_request(self, text: str):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')

        # Break Down request line into components
        (
            self.request_method,    # GET
            self.path,              # /hello
            self.request_version    # HTTP/1.1
        ) = request_line.split()

    def get_environ(self):
        env = {}
        """
            The following code snippet does not follow PEP8 conventions
            but it's formatted the way it is for demonstration purposes
            to emphasize the required variables and their values
        """
        # Required WSGI variables
        env["wsgi.version"]         = (1, 0)
        env["wsgi.url_scheme"]      = "http"
        env["wsgi.input"]           = io.StringIO(self.request_data)
        env["wsgi.errors"]          = sys.stderr
        env["wsgi.multithread"]     = False
        env["wsgi.multiprocess"]    = False
        env["wsgi.run_once"]        = False

        # Required CGI variables
        env["REQUEST_METHOD"]       = self.request_method      # GET
        env["PATH_INFO"]            = self.path                # /hello
        env["SERVER_NAME"]          = self.server_name         # localhost
        env["SERVER_PORT"]          = str(self.server_port)    # port: 8888
        return env
    
    def get_timestamp(self):
        current_datetime = datetime.datetime.now()
        formatted_time = current_datetime.strftime("%a, %d %b %Y %X", )
        timezone = pytz.timezone("Asia/Manila")

        utc_offset = int(timezone.utcoffset(current_datetime).total_seconds() / 3600.0)

        return f"{formatted_time} UTC+{utc_offset}"


    def start_response(self, status, response_headers, exec_info=None):
        # Add needed server headers
        server_headers = [
            ("Data", self.get_timestamp()),    # Example only
            ("server", "WSGIServer 1.2"),
        ]
        self.headers_set = [status, response_headers + server_headers]
    
    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = f"HTTP/1.1 {status}\r\n"

            for header in response_headers:
                response += "{0}: {1}\r\n".format(*header)
            response += '\r\n'

            for data in result:
                response += data.decode("utf-8")
            print("".join(f"> {line}\n" for line in response.splitlines()))         # Print fotmatted response data
            
            response_bytes = response.encode()
            self.client_connection.sendall(response_bytes)

        finally:
            self.client_connection.close()

SERVER_ADDRESS = (HOST, PORT) = "", 8888

def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Provide a WSGI application object as module:callable")
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)

    print(f"WSGIServer: Serving HTTP on port {PORT} ...\n")
    httpd.serve_forever()