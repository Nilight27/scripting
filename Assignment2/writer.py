
import json
import pwd
import grp
import socket

def MName():
    try:
        return socket.gethostname()
    except Exception:
        print(f'error getting computer name')
    

