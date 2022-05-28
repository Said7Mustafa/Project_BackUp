import os

# #this is the directory that i will compare to the backup directory, it will be saved to listby
# patha = 'S:\Information Technology\Python_WorkStation\Project_BackUp\start\\backup'
# listby = []
# for root, dirs, files in os.walk(patha):
#     data = root.replace(patha, '')
#     listby.append(data)
#     print(data)
#     for f in files:
#         listby.append('{}\{}'.format(data, f))
#         print('{}\{}'.format(data, f))
# listby = listby[1:]

# #this is the backup directory that will be comapred to
# pathb = 'S:\Information Technology\Python_WorkStation\Project_BackUp\start\mainfile'
# listbx = []
# for root, dirs, files in os.walk(pathb):
#     data = root.replace(pathb, '')
#     listbx.append(data)
#     print(data)
#     for f in files:
#         listbx.append('{}\{}'.format(data, f))
#         print('{}\{}'.format(data, f))
# listbx = listbx[1:]



# print("\n\n")
# print(listbx)
# print()
# print(listby)

# print("\n\n")
# flag = False
# x = len(listbx)
# for i in listby:
#     for j in listbx:
#         if i == j:
#             flag = False
#             break
#         else:
#             flag = True
#     if flag == True:
#         print(i)



#this is the backup directory that will be comapred to
# pathb = 'S:\Information Technology\Python_WorkStation\Project_BackUp\start\mainfile'
# listbx = []
# for root, dirs, files in os.walk(pathb):
#     data = root.replace(pathb, '').count(os.sep)
#     listbx.append(data)
#     print(data)
#     level = root.replace(pathb, '').count(os.sep)
#     indent = ' ' * 4 * (level)
#     for f in files:
#         listbx.append('{}\{}'.format(data, f))
#         print('{}\{}'.format(data, f))
# listbx = listbx[1:]

# pathb = 'S:\Information Technology\Python_WorkStation\Project_BackUp\start\\backup'
# for root, dirs, files in os.walk(pathb):
#     level = root.replace(pathb, '').count(os.sep)
#     indent = ' ' * 4 * (level)
#     print('{}{}/'.format(indent, os.path.basename(root)))
#     subindent = ' ' * 4 * (level + 1)
#     for f in files:
#         print('{}{}'.format(subindent, f))
        
