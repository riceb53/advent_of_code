f = open('day7inputtest.txt','r')
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

print(folder_path)
print(previous_folders)



# if you cd into something it gets added to folder_path
# if you ls count all the file sizes in the response
# if you cd ../ then remove that folder to the file path
