import pandas as pd
import numpy as np

def by_hand_mean(the_list: list) -> float:
    sum = 0
    for i in range(len(the_list)):
        sum += the_list[i]
    
    return sum / len(the_list)

def pandas_mean(pd_list: pd.DataFrame) -> float:
    mean_result = pd_list.mean()

    return float(mean_result[0])

def by_hand_median(the_list: list) -> float|int:
    the_list.sort()
    length = len(the_list)

    if length % 2 == 0:
        middle = int(length / 2)
        median = (the_list[middle-1] + the_list[middle]) / 2
    else:
        middle = int(length / 2)
        median = the_list[middle]

    return median

def pandas_median(pd_list: pd.DataFrame) -> float:
    median = pd_list.median()

    return float(median[0])

def by_hand_mode(the_list: list) -> float|int:
    count_nums = {}

    for i in range(len(the_list)):
        if the_list[i] not in count_nums.keys():
            count_nums[the_list[i]] = 1
        else:
            count_nums[the_list[i]] = count_nums[the_list[i]] + 1

    max_num = 0
    max_count = 0
    for i in count_nums.keys():
        if count_nums[i] > max_count:
            max_num = i
            max_count = count_nums[i]
    
    return max_num

def pandas_mode(pd_list: pd.DataFrame) -> float|int:
    mode_result = pd_list.mode()

    return mode_result[0][0]

def by_hand_sample_variance(the_list: list) -> float:
    bessel_correction = 1 / (len(the_list) - 1)
    list_mean = pandas_mean(pd.DataFrame(data=the_list))

    sum = 0
    for i in range(len(the_list)):
        sum += ((the_list[i] - list_mean) ** 2)
    
    variance = bessel_correction * sum

    return float(variance)

def pandas_variance(pd_list: pd.DataFrame) -> float|int:
    variance_result = pd_list.var()

    return float(variance_result[0])

if __name__ == "__main__":
    data1 = [
    12.5, 15.2, 13.1, 16.7, 14.8, 
    18.3, 19.5, 21.1, 17.2, 20.3,
    16.5, 22.8, 24.1, 25.7, 27.9,
    29.0, 18.6, 15.9, 14.3, 13.7,
    12.8, 11.4, 10.5, 30.2, 32.1
]
    data2 = [13, 15, 76, 85]

    data3 = [1, 1, 3, 5, 6, 7, 8, 2, 3, 1]

    by_hand_mean_result = by_hand_mean(data1)
    print("By hand mean result: ", by_hand_mean_result)

    pd_mean = pandas_mean(pd.DataFrame(data=data1))
    print("Pandas mean result: ", pd_mean)

    by_hand_median_result =  by_hand_median(data1)
    print("By hand median result: ", by_hand_median_result)
    
    pd_median = pandas_median(pd.DataFrame(data=data1))
    print("Pandas median result: ", pd_median)

    by_hand_mode_result = by_hand_mode(data3)
    print("By Hand mode result: ", by_hand_mode_result)

    pd_mode = pandas_mode(pd.DataFrame(data=data3))
    print("Pandas mode result: ", pd_mode)

    by_hand_sample_variance_result = by_hand_sample_variance(data1)
    print("By hand variance result: ", by_hand_sample_variance_result)

    pd_variance = pandas_variance(pd.DataFrame(data=data1))
    print("Pandas variance result: ", pd_variance)
