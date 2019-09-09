from scapy.all import *

pcaps=rdpcap(sys.argv[1])


f=open(sys.argv[1]+".txt",'a')

start_time=pcaps[0].time
end_time=pcaps[len(pcaps)-1].time
duration=end_time-start_time
total_byte=0
sd={}

for packet in pcaps:
	total_byte=total_byte+len(packet)
#	if (packet.src+"->"+packet.dst not in sd):
#		sd[packet.src+"-"+packet.dst]=1
#	else:
#		sd[packet.src+"-"+packet.dst]+=1
	





avg_byte=total_byte/duration
print >>f,"total_byte: %d "%(total_byte)
print>>f ,"avg_byte_per_second: %f \n"%(avg_byte)
print>>f ,"avg_packet_num_per_second: %f \n"%(len(pcaps)/duration)
print>>f ,"avg_packet_size: %f \n"%(total_byte/len(pcaps))
#f.writeline(sd)
f.close()
