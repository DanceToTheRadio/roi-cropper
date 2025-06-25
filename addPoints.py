# addPoints.py
# If there are less than 6 lines (pairs of points) in a file, adds 0s (specific requirement of my model)
# You probably won't need to use this code, but I'll leave it here just in case :)
import os

# path to your txt files
path = f"coordinates"


file_list = [f for f in os.listdir(path) if f.endswith('.txt')]
print(f"Number of elements: {len(file_list)}")

# add 0,0,0,0 lines to files which have less than 6 lines
for i, file_name in enumerate(file_list):
    with open(f"{path}/{file_name}", 'r+') as f:
        len = 0
        for l in f:
            len += 1
        print(f"{path}/{file_name}")
        print(len)
        if len < 6:
            to_append = '\n0,0,0,0'
            for i in range(len, 6):
                f.write(to_append)

# correct (remove) \n lines
lst = []   
for i, file_name in enumerate(file_list):
    txt = ''
    with open(f"{path}/{file_name}", 'r+') as f:
        len = 0
        for l in f:
            if l.rstrip() != '':
                txt += l
    lst.append(txt)

for i, file_name in enumerate(file_list):
    with open(f"{path}/{file_name}", 'w') as f:
        f.write(lst[i])
