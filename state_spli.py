import dpkt
import socket
import sys

f=open(sys.argv[1],'r')
pcap=dpkt.pcap.Reader(f)
i=0
last=''
last_ts=0
last_i=0
for ts,buf in pcap:
	i=i+1
	try:
		eth=dpkt.ethernet.Ethernet(buf)
		ip=eth.data
		src=socket.inet_ntoa(ip.src)
		dst=socket.inet_ntoa(ip.dst)
		if(src=="192.168.1.120" and dst=="239.192.15.255"):
			if (not buf[62]==last):
				if (ts-last_ts>5 and last_i!=0):
					print last_i,last_ts,i-1,ts,''.join(hex(ord(last)))
				last=buf[62]
				last_i=i
				last_ts=ts
	except:
		pass
print last_i,last_ts,''.join(hex(ord(last)))


f.close()
