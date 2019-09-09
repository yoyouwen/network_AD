python state_spli.py $1 > inter.txt

count=1
l=(0 0 0 0'\x0')
c=(0 0 0 0'\x0')
cat inter.txt | while read line
do
i=0
for item in $line
do
c[$i]=$item
i=$i+1
done

if [ $count -eq 1 ]
then
echo editcap -r $1 idle.pcap 0-${c[2]}
editcap -r $1 idle.pcap 0-${c[2]}
fi

if [ $count -eq 2 ]
then
echo editcap -r $1 loading.pcap ${c[0]}-${c[2]}
editcap -r $1 loading.pcap ${c[0]}-${c[2]}
fi

if [ $count -eq 3 ]
then
echo editcap -r $1 cycling.pcap ${c[0]}-${c[2]}
editcap -r $1 cycling.pcap ${c[0]}-${c[2]}
fi

if [ $count -eq 4 ]
then
echo editcap -r $1 unloading.pcap ${c[0]}-${c[2]}
editcap -r $1 unloading.pcap ${c[0]}-${c[2]}
fi


if [ $count -eq 5 ]
then
echo editcap -r $1 idle2.pcap ${c[0]}-99999999
editcap -r $1 idle2.pcap ${c[0]}-99999999
fi


count=`expr $count + 1`
echo $count
done


echo "done"
