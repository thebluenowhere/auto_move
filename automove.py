# automove.py

import glob
import os
import shutil

src_folder = "/home/elevynn/Downloads"
ebooks_folder = "/home/elevynn/Ebooks"
pdf_folder = "/home/elevynn/Documents/PDF"
music_folder = "/home/elevynn/Music"
docs_folder = "/home/elevynn/Documents"
pic_folder = "/home/elevynn/Pictures"


# search files by extension in source dir
ebook_ext = "/*.epub"
pdf_ext = "/*.pdf"
music_ext = "/*.mp3"
doc_ext = "/*.txt"
pic_ext = "/*.jpg"

ebook_files = glob.glob(src_folder + ebook_ext)
pdf_files = glob.glob(src_folder + pdf_ext)
music_files = glob.glob(src_folder + music_ext)
doc_files = glob.glob(src_folder + doc_ext)
pic_files = glob.glob(src_folder + pic_ext)

# move the files with epub extension
for file in ebook_files:
    # extract file name from file path
    file_name = os.path.basename(file)
    shutil.move(file, ebooks_folder)
    print('Moved:', file)

# move the files with pdf extension
for file in pdf_files:
    # extract file name from file path
    file_name = os.path.basename(file)
    shutil.move(file, pdf_folder)
    print('Moved:', file)

# move the files with music extension
for file in music_files:
    # extract file name from file path
    file_name = os.path.basename(file)
    shutil.move(file, music_folder)
    print('Moved:', file)

# move the files with txt extension
for file in doc_files:
    # extract file name from file path
    file_name = os.path.basename(file)
    shutil.move(file, docs_folder)
    print('Moved:', file)

# move the files with jpg extension
for file in pic_files:
    # extract file name from file path
    file_name = os.path.basename(file)
    shutil.move(file, pic_folder)
    print('Moved:', file)