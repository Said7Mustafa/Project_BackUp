import os

pathb = 'S:\Main Folder\Desktop\start\gello'
listbx = []
for root, dirs, files in os.walk(pathb):
    levelb = root.replace(pathb, '')
    listbx.append(levelb)
    print(levelb)
    for f in files:
        listbx.append('{}\{}'.format(levelb, f))
        print('{}\{}'.format(levelb, f))
listbx = listbx[1:]

pathb = 'S:\Main Folder\Desktop\start\hight'
listby = []
for root, dirs, files in os.walk(pathb):
    levelb = root.replace(pathb, '')
    listby.append(levelb)
    print(levelb)
    for f in files:
        listby.append('{}\{}'.format(levelb, f))
        print('{}\{}'.format(levelb, f))
listby = listby[1:]

print("\n\n")

print(listbx)
print()
print(listby)

print("\n\n")
flag = False
x = len(listbx)
for i in listby:
    for j in listbx:
        if i == j:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        print(i)
    


