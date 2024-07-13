name_list = list()
while True :
    b = input("Enter a number :")
    if b == "done" :
        break
    value = float(b)
    name_list.append(value)

average = sum(name_list)/len(name_list)
print("Average is :",average)