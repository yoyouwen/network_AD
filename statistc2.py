import dpkt
import socket
import sys
import numpy
import csv
import matplotlib.pyplot as plt

f=open(sys.argv[1],'r')
#ff=open(sys.argv[1]+".txt",'a')
pcap=dpkt.pcap.Reader(f)

i=0
last=''
last_ts={}
last_i={}
all_i={}
all_ts={}
rpi={}
sd={}
for ts,buf in pcap:
	i=i+1
	try:
		eth=dpkt.ethernet.Ethernet(buf)
		ip=eth.data
		src=socket.inet_ntoa(ip.src)
		dst=socket.inet_ntoa(ip.dst)
		if (src+"->"+dst not in sd):
			sd[src+"->"+dst]=1
			last_ts[src+"->"+dst]=ts
			last_i[src+"->"+dst]=i
			all_i[src+"->"+dst]=[i]
			all_ts[src+"->"+dst]=[ts]
		else:
			all_i[src+"->"+dst].append(i)
			all_ts[src+"->"+dst].append(ts)
			sd[src+"->"+dst]+=1
			if (src+"->"+dst not in rpi):
				rpi[src+"->"+dst]=[ts-last_ts[src+"->"+dst]]
				last_ts[src+"->"+dst]=ts
			else:
				rpi[src+"->"+dst].append(ts-last_ts[src+"->"+dst])
				last_ts[src+"->"+dst]=ts
			
	except:
		pass
#print(rpi)


ff=open(sys.argv[2],'w')
csv_write=csv.writer(ff)
csv_head=["s->d","std","mean","max","min","num"]
csv_write.writerow(csv_head)


x=range(len(rpi["192.168.1.41->192.168.1.120"]))
fig=plt.figure()
print(len(all_i["192.168.1.41->192.168.1.120"]),len(rpi["192.168.1.41->192.168.1.120"]))
plt.scatter(all_i["192.168.1.12->239.192.34.128"][1:],rpi["192.168.1.12->239.192.34.128"])
plt.show()

for key in rpi:

	rpi[key]=numpy.array(rpi[key])
	#print '%s'%(key)
	#print '%f'%(rpi[key].std())#,rpi[key].mean(),rpi[key].max(),rpi[key].min()
	csv_write.writerow([key,rpi[key].std(),rpi[key].mean(),rpi[key].max(),rpi[key].min(),sd[key]])
	

ff.close
f.close()
