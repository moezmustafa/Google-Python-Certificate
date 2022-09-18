import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    print(localhost)
    if localhost == '127.0.0.1':
        return True

def check_connectivity():
    request = requests.get("http://www.google.com")
    responses = request.status_code
    print(responses)
    if responses == 200:
        return True


check_connectivity()
check_localhost()