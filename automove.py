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
               
def new_entry():
    extension_list = []
    dir_name = input("What is the name of the file type? ")
    ask_ext = True
    while ask_ext == True:
        extension = input("What extension do you want to monitor? ")
        extension_list.append(extension)
        choice = input("Do you want to add another extension? Type Yes/No ")
        if choice.strip().lower() == "no":
            f_path = input("Type in the file path: ")
            f_key = {f"folder": f"{f_path}"}
            combined_data['move_data'][dir_name] = {"folder": f_path}
            ext_key = {f"ext": f"{extension_list}"}
            combined_data['move_data'][dir_name] = {"ext": ext_key}
            ask_ext = False
        print(combined_data)

combined_data = {
    'src_folder': f'/home/elevynn/Downloads',
    'move_data': {
        'ebooks': {
            'folder': f'/home/elevynn/Ebooks',
            'ext': ['/*.epub', '/*.mobi', '/*.azw3']
        },
        'pdf': {
            'folder': f'/home/elevynn/Documents/PDF',
            'ext': ['/*.pdf']
        },
        'music': {
            'folder': f'/home/elevynn/Music',
            'ext': ['/*.mp3', '/*.aac', '/*.FLAC', '/*.mp4']
        },
        'docs': {
            'folder': f'/home/elevynn/Documents',
            'ext': ['/*.docx', '/*.txt']
        },
        'pic': {
            'folder': f'/home/elevynn/Pictures',
            'ext': ['/*.jpg', '/*.png']
        }
    }
}

new_entry()
if(__name__ == '__main__'):
    main()
