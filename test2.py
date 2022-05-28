import os

def get_File_Size(path):
    size = os.path.getsize(path) 
    return size

def get_Directory_Size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

print(get_Directory_Size('S:\Information Technology\Python_WorkStation\Project_BackUp\start\\backup'), 'bytes')

