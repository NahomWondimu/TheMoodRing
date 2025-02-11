import csv
from scapy.all import sniff
from datetime import datetime

# Open a CSV file to write the captured packet information
output_file = 'captured_packets.csv'

# Define the CSV headers
headers = ['Timestamp', 'Source IP', 'Destination IP', 'Protocol', 'Source Port', 'Destination Port', 'Packet Summary']

# Open the file in write mode and create the CSV writer
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

# Define a callback function to process each captured packet
def packet_callback(packet):
    # Prepare data to write into the CSV
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        protocol = packet.proto
        src_port = dst_port = None
        
        # If it's a TCP packet
        if packet.haslayer('TCP'):
            src_port = packet['TCP'].sport
            dst_port = packet['TCP'].dport
        
        # If it's a UDP packet
        elif packet.haslayer('UDP'):
            src_port = packet['UDP'].sport
            dst_port = packet['UDP'].dport
        
        # Prepare the row for the CSV
        packet_summary = packet.summary()
        row = [timestamp, ip_src, ip_dst, protocol, src_port, dst_port, packet_summary]
        
        # Write the packet data into the CSV file
        with open(output_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

        # Optionally print the packet details to the console
        print(f"{timestamp} - {ip_src} -> {ip_dst} | Protocol: {protocol} | TCP Port: {src_port} -> {dst_port}")
        print(f"Summary: {packet_summary}")
        print('-' * 80)

# Start sniffing the network, applying the callback function to each packet
sniff(prn=packet_callback, store=0)
