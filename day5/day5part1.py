# double check input example
    # generate lists for each stack

# parse directions



f = open('day5input.txt','r')
lines = f.read().split("\n\n")
stacks = lines[0]
directions = lines[1].split("\n")

def column_lookup(index):
    return int((index + 3) / 4)

stacks_split = stacks.split("\n")

all_stacks = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

for row in stacks_split:
    i = 1
    while (i < len(row)):
    # for character in row[1::4]:
        if row[i].isalpha():
            column = column_lookup(i)
            all_stacks[column - 1].insert(0, row[i])                        
        i += 4

# print(all_stacks)


for direction in directions:
    parts = direction.split(" ")
    count = int(parts[1])
    from_container = int(parts[3])
    to_container = int(parts[5])    
    for x in range(0, count):        
        all_stacks[to_container - 1].append(all_stacks[from_container - 1].pop())    
# print(all_stacks)    

top_crates = ""
for stack in all_stacks:
    print(stack[-1])
    top_crates += stack[-1]
print(top_crates)
# print("hbtm")
    # break
    # to_container.push(from_container.pop())
    




# 1,5,9,13,17,21,25,29,33

# fqllnm