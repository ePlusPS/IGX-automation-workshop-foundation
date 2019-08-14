#!/usr/bin/env python

from pandriver import *
from getpass import getpass
import sys

hostname = input("Device hostname: ")
username = input("Device username: ")
password = getpass("Device password: ")

try:
    pano = pandevice.panorama.Panorama(hostname, username, password)
    print(f'Panorama system info: {pano.refresh_system_info()}\n')
except:
    print('Failed to connect to Panorama')
