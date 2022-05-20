import os
# def list_files(startpath):
#     for root, dirs, files in os.walk(startpath):
#         level = root.replace(startpath, '').count(os.sep)
#         indent = ' ' * 4 * (level)
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
#         for f in files:
#             print('{}{}'.format(subindent, f))

# list_files('S:\Main Folder\Desktop\start')



# patha = 'S:\Main Folder\Desktop\start\hight'
# lista = []
# for root, dirs, files in os.walk(patha):
#     levela = root.replace(patha, '')
#     lista.append(levela)
#     # print(levela)
#     for f in files:
#         lista.append('{}\{}'.format(levela, f))
#         # print('{}\{}'.format(levela, f))

# # print(lista)


# pathb = 'S:\Main Folder\Desktop\start\gello'
# listb = []
# for root, dirs, files in os.walk(pathb):
#     levelb = root.replace(pathb, '')
#     listb.append(levelb)
#     # print(levela)
#     for f in files:
#         listb.append('{}\{}'.format(levelb, f))
#         # print('{}\{}'.format(levelb, f))
        
# print(listb)



# for i in lista:
#     for j in listb:
#         # print(i)
#         if i not in listb:
#             print(i)
#             break
            




pathb = 'S:\Main Folder\Desktop\start\gello'
listbx = []
listby = []
for root, dirs, files in os.walk(pathb):
    levelb = root.replace(pathb, '')
    listbx.append(levelb)
    print(levelb)
    for f in files:
        listby.append('{}\{}'.format(levelb, f))
        print('{}\{}'.format(levelb, f))
        
# print(listbx[1])
# x = len(listbx)
# for i in range(x):
#     print(listbx[i], listby[i], sep = ' ')

