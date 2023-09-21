# SCAPY Simple Packet Tracer with DNS Poisoning

## Description

This is a simple packet tracer, written in python.
It uses the all-mighty Scapy in order to trace and manipulate network traffic.
It filters DNS questions and sends a malformed DNS answers to the DNS server.
thus, it performs DNS Poisoning, as long as it reaches the DNS server fast enough.

## Getting Started

### Running the script

1.Run as root
```
python3 dnspois.py
```

### Run Example
```
172.12.34.56
.
Sent 1 packets.
b'example.org.'
172.12.34.56
.
Sent 1 packets.
b'shadow.com.'
172.12.34.56
.
Sent 1 packets.
b'furtheritwinds.de.'
172.12.34.56
.
Sent 1 packets.
b'letloosethehounds.co.uk.'
172.12.34.56
.
Sent 1 packets.
b'dineritnow.com.'
172.12.34.56
.
Sent 1 packets.
b'tictoc.org.'
```
