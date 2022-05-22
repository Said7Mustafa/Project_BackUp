
import os

#this will save the directory to a list
def directory_List(path):
    list = []
    for root,dirs, files in os.walk(path):
        level = root.replace(path, '')
        list.append(level)
        for f in files:
            list.append('{}\{}'.format(level, f))
    list = list[1:]
    return list

thiss = directory_List('S:\Main Folder\Desktop\start\gello')
print(thiss)

#this will display/print everything on that directory
def display_Directory_Tree(pathb):
    pathb = 'S:\Main Folder\Desktop\start\gello'
    for root, dirs, files in os.walk(pathb):
        levelb = root.replace(pathb, '')
        for f in files:
            print('{}\{}'.format(levelb, f))

# display_Directory_Tree('S:\Main Folder\Desktop\start\gello')

listbx = directory_List('S:\Main Folder\Desktop\start\mainfile')
listby = directory_List('S:\Main Folder\Desktop\start\\backup')

# print("\n\n")
print(listbx)
# print()
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


