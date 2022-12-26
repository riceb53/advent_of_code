# find how many characters before consecutive unique 4 characters
import pdb

f = open('day6input.txt','r')
lines = f.read()

# lines = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def find_unique_four(lines):
    for idx, character in enumerate(lines):
        # print(lines[idx],lines[idx + 1],lines[idx + 2],lines[idx])
        i = 1        
        if len(set([
            lines[idx],
            lines[idx + 1],
            lines[idx + 2],
            lines[idx + 3],
            lines[idx + 4],
            lines[idx + 5],
            lines[idx + 6],
            lines[idx + 7],
            lines[idx + 8],
            lines[idx + 9],
            lines[idx + 10],
            lines[idx + 11],
            lines[idx + 12],
            lines[idx + 13],
        ])) == 14:
            # pdb.set_trace()
            print([lines[idx],lines[idx + 1],lines[idx + 2],lines[idx + 3]])
            print(idx + 14)
            return idx + 13
    # print(idx, character)
    # print(lines[idx + 1])

find_unique_four(lines)
# print(lines)