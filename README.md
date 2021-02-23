# scapy_three_way_handshake
Establish three way handshake with scapy

## Usage 
### Disable output TCP RST
```
iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
```
The kerenl will reply RST if it receives a SYN-ACK but didn't send SYN.

So, disable output RST by iptables to prevent this situation.

### Run
```
python3 main.c
```
