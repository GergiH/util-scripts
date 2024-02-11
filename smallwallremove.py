import sys
from os import listdir, remove
from os.path import isfile, join
from PIL import Image

folder = sys.argv[1]
size = int(sys.argv[2])

if folder is None or size is None:
    print('Need both folder and size arguments')
    sys.exit()

files_to_delete = []

print(f'Removing smaller than {size}p JPGs and PNGs from folder: {folder}\n')

filenames_in_folder = [f for f in listdir(folder) if isfile(join(folder, f))]

for f in filenames_in_folder:
    filename = join(folder, f)

    with Image.open(filename) as img:
        width, height = img.size

        if height < size:
            files_to_delete.append(filename)

if len(files_to_delete) > 0:
    for f in files_to_delete:
        print(f)
    print()

    answer = ''
    while answer != 'y' and answer != 'n':
        answer = input('Are you sure you want to delete these files? (y/n) ')
    
    if answer == 'y':
        for f in files_to_delete:
            remove(f)
        print('Removed smaller images')
    else:
        print('Removed nothing')
else:
    print('Nothing to remove')
