file_list=("idle.pcap" "loading.pcap" "cycling.pcap" "unloading.pcap" "idle2.pcap")

for item in ${file_list[@]}
do
echo $item
python3 statistc.py $item 
done


for item in ${file_list[@]}
do
echo $item
python statistc1.py $item
done

