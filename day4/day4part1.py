# find all overlapping days
    # go to each row, find each day for both of them
    # if they completely overlap, count += 1
# count them

f = open('day4input.txt','r')
lines = f.read().split("\n")
count = 0
for line in lines:
    worker1_range = line.split(",")[0]
    worker2_range = line.split(",")[1]
    worker1_start = int(worker1_range.split("-")[0])
    worker1_stop = int(worker1_range.split("-")[1])
    worker2_start = int(worker2_range.split("-")[0])
    worker2_stop = int(worker2_range.split("-")[1])
    worker1_list = list(range(worker1_start, worker1_stop + 1))
    print(worker1_list)
    worker2_list = list(range(worker2_start, worker2_stop + 1))
    print(worker2_list)
    # print(worker1_start, worker1_start)
    working_overlap = set(worker1_list).issubset(worker2_list) | set(worker2_list).issubset(worker1_list)
    if working_overlap:
        count += 1
    print("***")
    # print(result)
print(count)
print(total_count)