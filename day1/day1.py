# part one
f = open('day1input.txt', 'r')
food = f.read().split("\n")
# print(food)
f.close()


top_three_food_carriers = [0,0,0]
current_elf_food = 0
for item in food:
    if item == '':
        if current_elf_food > top_three_food_carriers[-1]:
            for idx, food_carrier in enumerate(top_three_food_carriers):
                if current_elf_food > food_carrier:
                    top_three_food_carriers.insert(idx, current_elf_food)
                    top_three_food_carriers.pop()
                    break            
        current_elf_food = 0
    else:        
        current_elf_food += int(item)
print(sum(top_three_food_carriers))

