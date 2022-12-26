import pdb

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

# # print(all_stacks)
# all_stacks = [
#     ['z', 'n'],
#     ['m', 'c', 'd'],
#     ['p']
# ]


# directions = [
#     'move 1 from 2 to 1',
#     'move 3 from 1 to 3',
#     'move 2 from 2 to 1',
#     'move 1 from 1 to 2',
# ]

for direction in directions:
    parts = direction.split(" ")
    count = int(parts[1])
    from_container = int(parts[3])
    to_container = int(parts[5])    
    print("before")
    print(all_stacks)
    print(count)
    # pdb.set_trace()
    # find all the crates, keep the order, add them to the correct stack
    containers_to_move = all_stacks[from_container - 1][-count::]
    containers_to_stay = all_stacks[from_container - 1][:-count:]   
    all_stacks[to_container - 1] += containers_to_move
    all_stacks[from_container - 1] = containers_to_stay
    print("after")
    print(all_stacks)
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