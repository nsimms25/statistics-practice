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

    if length % 2 == 1:
        middle = int(length / 2)
        median = the_list[middle]

    return median # type: ignore

def pandas_median(pd_list: pd.DataFrame) -> float:
    median = pd_list.median()

    return float(median[0])

if __name__ == "__main__":
    data1 = [
    12.5, 15.2, 13.1, 16.7, 14.8, 
    18.3, 19.5, 21.1, 17.2, 20.3,
    16.5, 22.8, 24.1, 25.7, 27.9,
    29.0, 18.6, 15.9, 14.3, 13.7,
    12.8, 11.4, 10.5, 30.2, 32.1
]
    data2 = [13, 15, 76, 85]

    by_hand_mean_result = by_hand_mean(data1)
    print("By hand mean result: ", by_hand_mean_result)

    pd_mean = pandas_mean(pd.DataFrame(data=data1))
    print("Pandas mean result: ", pd_mean)

    by_hand_median_result =  by_hand_median(data1)
    print("By hand median result: ", by_hand_median_result)
    
    pd_median = pandas_median(pd.DataFrame(data=data1))
    print("Pandas median result: ", pd_median)
