#!C:\Python27\python.exe

# q1: hits to page

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip_address, identity, username, datetime, timezone, method, path, proto, status, size = data
        print path

