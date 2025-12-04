import os, shutil, traceback, time

folderPath = "your_folder_path_here"
backupPath = "your_backup_path_here"
interval = 300

def isExists(path):
    if (os.path.exists(path)) and (os.path.isdir(path)): # if path exists and is a directory
        return True
    else:
        return False
    
def listContent(path): # make function to create list of content and push it to an array
    list = []
    tree = os.walk(path)
    for (root,dirs,files) in tree:
        for f in files:
            # we need relative to properly compare content of both dirs
            relPath = os.path.relpath(os.path.join(root, f), path) # remove second arg from first arg
            list.append(relPath) # add to array
            
    return list # return array

def checkTimeAndSize(file1, file2):
    f1Time = os.path.getmtime(file1) 
    f2Time = os.path.getmtime(file2)

    f1Size = os.path.getsize(file1) 
    f2Size = os.path.getsize(file2)

    if ((f2Time - f1Time) > 2) or (f1Size != f2Size): 
        return False
    else:
        return True

def backupFile(src, dst):
    if os.path.exists(dst): 
        print(str(dst) + " is out of date.") # if file already exists, print this msg
    else: 
        print(str(dst) + " hasn't been backed up.")

    print("Backing up: " + str(dst) + " now...")
    if shutil.copy2(src, dst):
        print(str(dst) + " is now up to date.\n")
        return True
    else:
        print("Failed to backup!")
        return False

if isExists(folderPath):
    if isExists(backupPath):
        while True:
            # check files block
            folderFiles = listContent(folderPath) # list content of two dirs
            backupFiles = listContent(backupPath)
            finished = False
            
            if not finished:
                try:
                    # [:] - iterate through a copy of backupFiles
                    for i in backupFiles[:]: # check for files in backup that are missing in folder and remove them
                        if i not in folderFiles:
                            backupFiles.remove(i)

                    if (folderFiles == backupFiles):
                        # compare last modified date and size

                        for i in range(len(folderFiles)): # go through each file
                            a = os.path.join(folderPath, folderFiles[i]) # get abs path 
                            b = os.path.join(backupPath, backupFiles[i])

                            if checkTimeAndSize(a, b):
                                # if same time and size, leave backup file as is
                                pass
                                finished = True
                            else: 
                                # update backup file
                                backupFile(a, b) # a = file to backup, b = destination

                    else:
                        # check which files are missing from backup directory
                        missingFiles = len(folderFiles) - len(backupFiles)
                        print(str(missingFiles) + " file(s) are missing from the backup folder.")
                        print("Backing up missing files now...\n")

                        for i in folderFiles: # if there are missing files in backup
                            if i not in backupFiles:
                                x = os.path.join(folderPath, i)
                                y = os.path.join(backupPath, i)
                                # get directory path
                                head, sep, tail = y.rpartition("\\") # separate on rightmost \
                                z = head

                                os.makedirs(z, exist_ok=True) # ok even if dir already exists
                                backupFile(x, y)

                except Exception:
                    print(traceback.format_exc()) # print error
            print("Backup folder is up to date.")
            time.sleep(interval)
    else:
        print("Invalid backup path given.")
else: 
    print("Invalid folder path given.")