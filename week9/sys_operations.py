import platform
import socket
import os

print("Current Machine Type")
print(platform.machine())
print("==========================")

print("Current Processor Type")
print(platform.architecture)
print("==========================")

print("Set Socket Timeout to 50 Seconds")
print(socket.setdefaulttimeout(50))
print("Get the current Socket Timeout")
print(socket.getdefaulttimeout())
print("==========================")

print("Get current Operating System Type")
print(os.name)
print("Get current Operating System Name")
print(platform.name)
print("==========================")