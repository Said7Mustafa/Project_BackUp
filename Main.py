import os

def main():
    # thiss = directory_List('S:\Information Technology\Python_WorkStation\Project_BackUp\start\\backup')
    # print(thiss)
    
    # display_Directory_Tree('S:\Information Technology\Python_WorkStation\Project_BackUp\start\\backup')
    # print("\n\n")
    # display_Directory_Tree('S:\Information Technology\Python_WorkStation\Project_BackUp\start\mainfile')
    
    list_mainfile = directory_List('S:\Information Technology\Python_WorkStation\Project_BackUp\start\mainfile')
    list_backup = directory_List('S:\Information Technology\Python_WorkStation\Project_BackUp\start\\backup') 
    
    display_Compare_Directory_Tree(list_mainfile, list_backup) 
    
    
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


#this will display/print everything on that directory
def display_Directory_Tree(path):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def display_Compare_Directory_Tree(list_mainfile,list_backup):
    flag = False
    x = len(list_mainfile)
    for i in list_mainfile:
        for j in list_backup:
            if i == j:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            print(i)


def get_Directory_Size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

main()
