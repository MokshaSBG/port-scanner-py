import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)                     # don't wait forever
        result = s.connect_ex((host, port)) # 0 = success, other = error code
        s.close()
        return result == 0
    except Exception:
        return False

# Test it
print(scan_port("scanme.nmap.org", 80))   # True
print(scan_port("scanme.nmap.org", 9999)) # False (probably)
