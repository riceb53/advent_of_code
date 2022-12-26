# find how many characters before consecutive unique 4 characters
import pdb

f = open('day6input.txt','r')
lines = f.read()

# lines = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def find_unique_four(lines):
    for idx, character in enumerate(lines):
        # print(lines[idx],lines[idx + 1],lines[idx + 2],lines[idx])
        if len(set([lines[idx],lines[idx + 1],lines[idx + 2],lines[idx + 3]])) == 4:
            # pdb.set_trace()
            print([lines[idx],lines[idx + 1],lines[idx + 2],lines[idx + 3]])
            print(idx + 4)
            return idx + 4
    # print(idx, character)
    # print(lines[idx + 1])

find_unique_four(lines)
# print(lines)