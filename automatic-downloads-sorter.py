import os
import shutil
from pathlib import Path
import time

# The path to the directory we're working with
downloads_folder_path = r"C:\Users\user1\Downloads"

# Store the names of the folders we want, and the extension types that we want to be associated with each
folder_names = {
    "Audio": {'.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma'},
    "Compressed":{'.7z','.deb','.pkg','.rar','.rpm','.z', '.zip'},
    'Code':{'.js','.jsp','.html','.ipynb','.py','.java','.cpp'},
    'Documents':{'.ppt','.pptx','.xls', '.xlsx','.doc','.docx','.txt', '.tex', '.epub'},
    'Images':{'.bmp','.gif','.ico','.jpeg','.jpg','.png','.jfif','.svg','.tif','.tiff'},
    'Scanned':{'.pdf'},
    'Softwares':{'.apk','.bat','.bin', '.exe','.jar','.msi','.py'},
    'Videos':{'.3gp','.avi','.flv','.h264','.mkv','.mov','.mp4','.mpg','.mpeg','.wmv'},
    'Others': {'NONE'}
}

# Invert the above dictionary to create a map from each extension to its corresponding folder
filetype_map = {}
for filetype, extensions in folder_names.items():
    for extension in extensions:
        filetype_map[extension] = filetype


def run_sorter():
    # Change the current working directory to the Downloads folder (where we want to make our changes)
    os.chdir(downloads_folder_path)

    # Make the subfolders if they don't already exist
    for folder_name in folder_names.keys():
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

    # Iterate through the contents of the directory, using the filetype map to sort the files
    for file in os.listdir():
        if file in folder_names:
            continue
        elif os.path.splitext(file)[1] in filetype_map:
            shutil.move(file, filetype_map[os.path.splitext(file)[1]])
        else:
            shutil.move(file, "Others")

    return


print("RUNNING DOWNLOADS SORTER")
run_sorter()

# Checks the state of the downloads folder every XX seconds, calling the sorter if a change in the number of files is detected
while True:
    num_files = len(os.listdir(downloads_folder_path))
    old_num = num_files
    time.sleep(20)
    num_files = len(os.listdir(downloads_folder_path))
    
    if num_files != old_num:
        print("RUNNING DOWNLOADS SORTER")
        run_sorter()