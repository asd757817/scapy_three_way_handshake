from scapy.all import *

sport = random.randint(1024,65535)
dport = 80

# SYN
ip=IP(src="192.168.1.123", dst="10.10.0.123")
TCP_SYN=TCP(sport=sport, dport=dport, flags="S", seq=1000)

# SYN-ACK
TCP_SYNACK=sr1(ip/TCP_SYN)

# ACK
my_ack = TCP_SYNACK.seq + 1
TCP_ACK=TCP(sport=sport, dport=dport, flags="A", seq=TCP_SYNACK.ack, ack=my_ack)
send(ip/TCP_ACK)

# PUSH
payload = "test"
TCP_PUSH=TCP(sport=sport, dport=dport, flags="PA", seq=TCP_SYNACK.ack, ack=my_ack)
send(ip/TCP_PUSH/payload)
