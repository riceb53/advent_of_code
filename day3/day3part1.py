# split each item in half
# find the common term between the strings
# find the priority for each common term
# sum them

f = open('day3input.txt','r')
lines = f.read().split("\n")
# print(lines)

sum_of_priorities = 0
for line in lines:
  firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
  repeat_item = ''.join(set(firstpart).intersection(secondpart))
  if repeat_item.capitalize() == repeat_item:
    print(repeat_item)
    print(ord(repeat_item) - 38)
    sum_of_priorities += ord(repeat_item) - 38
    print("**")
  else:
    print(repeat_item)
    print(ord(repeat_item) - 96)
    sum_of_priorities += ord(repeat_item) - 96



print(sum_of_priorities)
