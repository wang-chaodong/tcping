#!/usr/bin/python3
import socket
import sys
import time
import datetime


def check_port(ip, port):
    requestsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    requestsocket.settimeout(3)
    res = True
    try:
        requestsocket.connect((ip, int(port)))
    except Exception:
        res = False
    requestsocket.close()
    return res


if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    i = 0
    while True:
        i += 1
        st = datetime.datetime.now()
        if check_port(ip, port):
            et = datetime.datetime.now()
            ms = round((et.timestamp() - st.timestamp()) * 1000, 2)
            print("Connect to %s[%s] seq=%d time=%s" % (ip, port, i, ms))
        else:
            print("Connect to %s[%s] seq=%d is timeout." % (ip, port, i))
        time.sleep(1)
