fname = input("Enter file name: ")
fh = open(fname)
lst = list()
 
for line in fh:
    line = line.strip()
    words = line.split()  #split the  line in list of the words
    
    for word in words :
        
        if word not in lst :
            lst.append(word)
            
lst.sort()
print(lst)
