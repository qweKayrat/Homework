from os.path import isdir, getsize, join
from os import listdir


def print_info_directory(directory):
    for i in listdir(directory):
        j = join(directory, i)
        if isdir(j):
            print(i, '- dir -', getsize(j), 'bytes')
        else:
            print(i, '- file -', getsize(j), 'bytes')


print_info_directory(r'C:\Python215\Python\work\venv')
