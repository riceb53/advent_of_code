# split into groups of three
# find common character in all three
# find the priority
# sum them



f = open('day3input.txt','r')
lines = f.read().split("\n")
# print(lines)
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

 
chunks = divide_chunks(lines, 3)
sum_of_priorities = 0
for chunk in chunks:
  unique_character = ''.join(set(chunk[0]).intersection(chunk[1]).intersection(chunk[2]))
  print(unique_character)
  if unique_character.capitalize() == unique_character:
    print(unique_character)
    print(ord(unique_character) - 38)
    sum_of_priorities += ord(unique_character) - 38
    print("**")
  else:
    print(unique_character)
    print(ord(unique_character) - 96)
    sum_of_priorities += ord(unique_character) - 96

print(sum_of_priorities)
