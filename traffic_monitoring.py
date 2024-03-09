import pcapy
import socket
import struct
import sqlite3
from datetime import datetime

# Function to convert binary IP address to string
def ip_to_str(address):
    return socket.inet_ntoa(struct.pack('!I', address))

# Function to handle captured packets
def packet_handler(header, data):
    eth_length = 14

    # Parse IP header
    ip_header = data[eth_length:20+eth_length]
    iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4

    src_ip = ip_to_str(iph[8])

    # Log IP address and timestamp to database
    log_ip(src_ip)

# Function to log IP address to database
def log_ip(ip):
    conn = sqlite3.connect('traffic_log.db')
    cursor = conn.cursor()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("INSERT INTO traffic_log (ip_address, timestamp) VALUES (?, ?)", (ip, timestamp))
    conn.commit()

    conn.close()

def main():
    # Open network interface for capturing packets (replace 'eth0' with your network interface)
    cap = pcapy.open_live('eth0', 65536, 1, 0)

    # Set packet filter to capture only IP packets
    cap.setfilter('ip')

    # Create database table if not exists
    conn = sqlite3.connect('traffic_log.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS traffic_log (
                        id INTEGER PRIMARY KEY,
                        ip_address TEXT,
                        timestamp TIMESTAMP)''')
    conn.commit()
    conn.close()

    # Start capturing packets
    while True:
        (header, data) = cap.next()
        packet_handler(header, data)

if __name__ == "__main__":
    main()
