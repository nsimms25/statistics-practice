import pandas as pd

print(pd.__version__)

data = [1,1,2,2,3,4,4,5,6,6,6]

count_nums = {}

for i in range(len(data)):
    if data[i] not in count_nums.keys():
        count_nums[data[i]] = 1
    else:
        count_nums[data[i]] = count_nums[data[i]] + 1

print(count_nums)
print(count_nums.keys())


max_num = 0
max_count = 0
for i in count_nums.keys():
    #print(count_nums[i])
    if count_nums[i] > max_count:
        max_num = i
        max_count = count_nums[i]

print(max_num)
print(max_count)
