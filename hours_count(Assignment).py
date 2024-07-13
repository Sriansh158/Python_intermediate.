name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

hour_count = dict()

for line in handle :
    line = line.rstrip()
    
    if line.startswith("From "):
        words = line.split()
        
        time_part = words[5]
        
        hours = time_part.split(":")
        
        hour = hours[0]
        hour_count[hour] = hour_count.get(hour,0) +1
       
        
sorted_hours = sorted(hour_count.items())

for hour , count in sorted_hours :
    print(hour,count)
        
