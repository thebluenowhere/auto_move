import glob
import os
import shutil

combined_data = {
    "src_folder": "/home/elevynn/Downloads",
    "move_data": {
        "ebooks": {
            "folder": "/home/elevynn/Ebooks",
            "ext": ["/*.epub", "/*.mobi", "/*.azw3"]
        },
        "pdf": {
            "folder": "/home/elevynn/Documents/PDF",
            "ext": ["/*.pdf"]
        },
        "music": {
            "folder": "/home/elevynn/Music",
            "ext": ["/*.mp3", "/*.aac", "/*.FLAC", "/*.mp4"]
        },
        "docs": {
            "folder": "/home/elevynn/Documents",
            "ext": ["/*.docx", "/*.txt"]
        },
        "pic": {
            "folder": "/home/elevynn/Pictures",
            "ext": ["/*.jpg", "/*.png"]
        }
    }
}

src_folder = combined_data['src_folder']
data = combined_data['move_data']

for item in data:
    folder = data[item]["folder"]
    exts = data[item]['ext']
    for ext in exts:
        files = glob.glob(src_folder + ext)

        for file in files: 
            file_name = os.path.basename(file)
            shutil.move(file, folder)
            print('Moved:', file)

    