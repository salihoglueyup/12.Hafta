import socket

remote_host=socket.gethostname()
remote_port=8880
# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the remote host and port
sock.connect(("127.0.0.1",8880))
# Send a request to the host
sock.send(b"Why don't you call me any more?")
# Get the host's response, no more than, say, 1,024 bytes
response_data = sock.recv(1024)
# Terminate
sock.close( )
