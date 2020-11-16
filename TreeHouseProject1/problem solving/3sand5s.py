eulerlist = []

for i in range(1,1000):
    if int(i)%3 == 0:
        eulerlist.append(int(i))
    if int(i)%5 == 0:
        eulerlist.append(int(i))

eulerset = set(eulerlist)
print(sum(eulerset))
    
