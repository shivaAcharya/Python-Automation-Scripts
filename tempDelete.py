"""
Inspired From:

https://github.com/NavjotSingh007/windows-temporary-file-cleaner/blob/master/TempClean.py

"""

import os
import shutil
    
folders = ['C:/Users/'+os.getlogin()+'/AppData/Local/Temp',
            'C:/Windows/Temp', 
            'C:/Windows/Prefetch']


deleteFileCount = 0
deleteFolderCount = 0

for folder in folders:
    print(f"\n################# DELETING FROM {folder.split('/')[-1]} ###########\n")
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"{the_file} file deleted")
                deleteFileCount += 1

            elif os.path.isdir(file_path):
                #if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                print(f"{the_file} folder deleted")
                deleteFolderCount += 1

        except Exception as e:
            print(f"Access Denied:{the_file}")

print ("\n################## REPORT ###############\n")
print(f"{deleteFileCount} files and {deleteFolderCount} folders deleted.")
input('Press <Enter> to Exit')
