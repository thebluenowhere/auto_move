import glob
import os
import shutil
import json

f = open('config.json')

combined_library = json.load(f)

def main():
    src_folder = combined_library['src_folder']
    data = combined_library['move_data']
    move_files(src_folder, data)

def move_files(src_folder, data):
    for item, value in data.items():
        folder = value['folder']
        exts = value['ext']
        for ext in exts:
            files = glob.glob(src_folder + ext)

            for file in files:
                file_name = os.path.basename(file)
                shutil.move(file, folder)
                print('Moved:', file)

if(__name__ == '__main__'):
    main()
