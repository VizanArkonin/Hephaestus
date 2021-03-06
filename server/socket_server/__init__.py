"""
Socket server.
Provides low-level connection interface for Orange PI boards. 1 Instance of socket server is run on host
and 1 Instance of client is run on single given board.
Server has it's own authentication system, data packets structure and uses AES encryption.
"""
from threading import Thread

import server.config as config
from server.socket_server.interface import SocketInterface
from server.socket_server.socket_server import SocketServer

# First, we create SocketServer instance and it's interface
__server = SocketServer(config.BOARD_SERVICE_CONFIG["host"], config.BOARD_SERVICE_CONFIG["port"])
server_interface = SocketInterface(__server)

# Then we import everything from respective routing library. DO NOT REMOVE THIS IMPORT!
import server.socket_server.routes


def listen():
    """
    Payload for server thread - keep listener up while being run from inside the thread.
    :return: None
    """
    try:
        __server.listen()
    except KeyboardInterrupt:
        __server.shut_down()


# Finally, we initiate the server thread and start it
server_thread = Thread(target=listen)
server_thread.start()
