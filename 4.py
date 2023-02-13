import socket
hostname=socket.gethostname()   
ip=socket.gethostbyname(hostname) 
print("Current ip address: ", ip)
