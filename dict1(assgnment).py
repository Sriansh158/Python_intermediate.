name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
    
handle = open(name)

dict ={}
count = 0

for line in handle :
    line =line.rstrip()
    
    if line.startswith("From "):
        words =line.split()
        email =words[1]
        
        dict[email] =dict.get(email,0) +1
        
        
max_count = None
name = None

for sender,count in dict.items() :
    
    if max_count is None or count > max_count :
        max_count =  count
        name = sender
print(name,max_count)
