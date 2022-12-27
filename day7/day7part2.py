import pdb
f = open('day7input.txt','r')
lines = f.read().split("\n")



folder_path = []
previous_folders = []

for line in lines:    
    if line.startswith('$ cd ..'):
        previous_folders.append(folder_path.pop())
        # remove from folder path
    elif line.startswith('$ cd'):
        # find the folder name add it to folder_path
        folder_name = line.split(" ")[-1]
        new_folder = {'name': folder_name, 'size': 0}        
        folder_path.append(new_folder)
    elif line[0].isdigit():
        # add size to all foldwere path
        size = line.split(" ")[0]
        for folder_dict in folder_path:
            folder_dict['size'] += int(size)

all_folders = folder_path + previous_folders

# sum = 0
# for folder in all_folders:
#     if folder['size'] <= 100000:
#        sum +=  folder['size']

# print(all_folders)
# print(sum)



total_space = 70_000_000
used_space = all_folders[0]['size']
remaining_space = total_space - used_space
necessary_space = 30_000_000
increase_space_by = necessary_space - remaining_space
# increase by at least
# 9_192_532
# 40_842_292

# sbtl
# 12_390_492




# sorted_folders = sorted(all_folders, key=lambda d: d['size']) 




# find the min fize folder that meets this requirement
# loop through, size - increase_space_by
min_folder = {'name': 'init', 'size': 70_000_000}
for folder in all_folders:
    # if folder['size'] - increase_space_by > 0 & folder['size'] < min_folder['size']:
    if (folder['size'] - increase_space_by > 0) & (folder['size'] < min_folder['size']):
        # pdb.set_trace()
        min_folder = folder
# if it's positive, see if it's smaller than current
print(min_folder['size'])


# if you cd into something it gets added to folder_path
# if you ls count all the file sizes in the response
# if you cd ../ then remove that folder to the file path
