# DGFN-2-Assgn-1-2023
# This server runs on the Raspberry Pi and sends arguments from vcgencmds as a JSON object.

# Necessary imports
import socket
import os
import json

# Setup the server socket
s = socket.socket()
host = '10.102.13.80'  # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

# Additional functions to handle vcgencmd calls
def get_temperature():
    temperature = os.popen('vcgencmd measure_temp').readline().strip()
    return temperature
        
def get_voltage():
    voltage = os.popen('vcgencmd measure_volts core').readline().strip()
    return voltage

def get_clock_speed():
    clock_speed = os.popen('vcgencmd measure_clock arm').readline().strip()
    return clock_speed

def get_memory_split():
    memory_split = os.popen('vcgencmd get_mem arm').readline().strip()
    return memory_split

def get_codec_info():
    codec_info = os.popen('vcgencmd codec_enabled H264').readline().strip()
    return codec_info


# Server main loop to handle incoming connections
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    
    # Get metrics
    temperature = get_temperature()
    voltage = get_voltage()
    clock_speed = get_clock_speed()
    memory_split = get_memory_split()
    codec_info = get_codec_info()
    
    print("Temperature:", get_temperature())
    print("Voltage:", get_voltage())
    print("Clock Speed:", get_clock_speed())
    print("Memory Split:", get_memory_split())
    print("CodecInfo:", get_codec_info())
    
    # Create a dictionary with all the metrics
    metrics_dict = {
        "Temperature": temperature,
        "Voltage": voltage,
        "ClockSpeed": clock_speed,
        "MemorySplit": memory_split,
        "CodecInfo": codec_info,
    }
    
    # Convert the dictionary to a JSON object
    metrics_json = json.dumps(metrics_dict)
    
    # Send the JSON object to the client
    c.sendall(metrics_json.encode())
    c.close()
