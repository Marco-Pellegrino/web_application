import os
from collections import defaultdict
from typing import ItemsView

FILE_TYPES = ('jpg','.png','.gif','.JPEG','.PNG')


os.chdir('assets/Example_Files')

example_collection = defaultdict(list)

for root, dirs, files in os.walk(os.getcwd()):

    if files:
        for file_names in files:
            file_name = os.path.join(root,file_names)
            if file_name.endswith(FILE_TYPES):
                example_name = file_name.split('/')[-3]
                example_collection[example_name].append(file_name)
                #print(example_collection)
                #print(file_name)


for k,v in example_collection.items():
    print(f'key = {k}')
    print(f'items = {v}')
    print( len(v))

