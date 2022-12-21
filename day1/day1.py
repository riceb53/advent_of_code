# part one

f = open('day1input.txt', 'r')
food = f.read().split("\n")
# print(food)
f.close()


max_food = 0
current_elf_food = 0
for item in food:
    if item == '':
        if current_elf_food > max_food:
            max_food = current_elf_food
        current_elf_food = 0
    else:        
        current_elf_food += int(item)
print(max_food)

