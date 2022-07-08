import glob
import os
import shutil
import json

with open ('config.JSON') as config_file:
    conf = json.load(config_file)
username = conf['username']


combined_data = {
    'src_folder': f'/home/{username}/Downloads',
    'move_data': {
        'ebooks': {
            'folder': f'/home/{username}/Ebooks',
            'ext': ['/*.epub', '/*.mobi', '/*.azw3']
        },
        'pdf': {
            'folder': f'/home/{username}/Documents/PDF',
            'ext': ['/*.pdf']
        },
        'music': {
            'folder': f'/home/{username}/Music',
            'ext': ['/*.mp3', '/*.aac', '/*.FLAC', '/*.mp4']
        },
        'docs': {
            'folder': f'/home/{username}/Documents',
            'ext': ['/*.docx', '/*.txt']
        },
        'pic': {
            'folder': f'/home/{username}/Pictures',
            'ext': ['/*.jpg', '/*.png']
        }
    }
}

def main():
    src_folder = combined_data['src_folder']
    data = combined_data['move_data']
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
