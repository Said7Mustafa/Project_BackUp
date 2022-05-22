import os

#this is the directory that i will compare to the backup directory, it will be saved to listby
patha = 'S:\Main Folder\Desktop\start\\backup'
listby = []
for root, dirs, files in os.walk(patha):
    levelb = root.replace(patha, '')
    listby.append(levelb)
    print(levelb)
    for f in files:
        listby.append('{}\{}'.format(levelb, f))
        print('{}\{}'.format(levelb, f))
listby = listby[1:]

#this is the backup directory that will be comapred to
pathb = 'S:\Main Folder\Desktop\start\mainfile'
listbx = []
for root, dirs, files in os.walk(pathb):
    levelb = root.replace(pathb, '')
    listbx.append(levelb)
    print(levelb)
    for f in files:
        listbx.append('{}\{}'.format(levelb, f))
        print('{}\{}'.format(levelb, f))
listbx = listbx[1:]


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

