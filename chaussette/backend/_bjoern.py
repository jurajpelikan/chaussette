"""
Bjoern backend.
https://github.com/jonashaag/bjoern
"""
import bjoern
import socket

from chaussette.util import create_socket


class Server(object):
    """
    Bjoern server wrapper.
    """
    def __init__(
        self, listener, application=None, backlog=2048,
        socket_type=socket.SOCK_STREAM, address_family=socket.AF_INET
    ):
        """
        Create socket.
        """
        host, port = listener

        self.application = application
        self.address_family = address_family
        self.socket_type = socket_type
        self.socket = create_socket(
            host,
            port,
            self.address_family,
            self.socket_type,
            backlog=backlog
        )
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_address = self.socket.getsockname()

    def serve_forever(self):
        """
        Run server.
        """
        bjoern.server_run(self.socket, self.application)
