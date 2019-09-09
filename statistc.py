import pyshark

import sys

def print_highest_layer(pkt):
	return pkt.highest_layer


def main():
	f=open(sys.argv[1]+".txt",'w')
	protocol={}
	protocol_tot_len={}
	protocol_len={}
	packet_num=0
	cap=pyshark.FileCapture(sys.argv[1])
	for packet in cap:
		packet_num+=1
		if ((packet.highest_layer) in protocol):
			protocol[packet.highest_layer]+=1
			protocol_tot_len[packet.highest_layer]+=int(packet.length,10)
			if not (packet.length in protocol_len[packet.highest_layer]):
				protocol_len[packet.highest_layer].append(packet.length)
		else:
			protocol[packet.highest_layer]=1
			protocol_tot_len[packet.highest_layer]=int(packet.length,10)
			protocol_len[packet.highest_layer]=[packet.length]
		print(packet_num)
	
	print(protocol,file=f)
	print(protocol_tot_len,file=f)
	print(protocol_len,file=f)	
	for key in protocol:
		protocol[key]=protocol[key]/packet_num
	print(protocol,file=f)
	f.close()

main()
