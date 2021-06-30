#!/usr/bin/python3
import random
import socket
import struct
import requests
import _thread

MAX_THREADS = 5


def find_ip():
    while True:
        try:
            # Generate Random IP
            url = 'http://' + socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

            # Known Working Case
            # url = "http://figrocloud.duckdns.org"

            r = requests.get(url).status_code

            if r == 200:  # Return URL on HTML 200 Response code (OK)
                print(url + ' Success\n')
        except requests.exceptions.ConnectionError:
            # Print failed ips
            # print(url + ' Failed\n')
            pass


for i in range(0, MAX_THREADS):
    try:
        _thread.start_new_thread(find_ip, ())
    except:
        print("thread could not start")
        exit()
while True:
    pass
