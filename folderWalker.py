import os

ch_dir = os.getcwd()


# print(os.listdir(ch_dir))


for dirpath, dirnames, filenames in os.walk(ch_dir):
    print(f'dirpath: {dirpath}')
    print(f'dirnames: {dirnames}')
    print(f'filenames: {filenames}')