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



if __name__ == "__main__":
    data = [
    12.5, 15.2, 13.1, 16.7, 14.8, 
    18.3, 19.5, 21.1, 17.2, 20.3,
    16.5, 22.8, 24.1, 25.7, 27.9,
    29.0, 18.6, 15.9, 14.3, 13.7,
    12.8, 11.4, 10.5, 30.2, 32.1
]
    by_hand_mean_result = by_hand_mean(data)
    print(by_hand_mean_result)

    pd_mean = pandas_mean(pd.DataFrame(data=data))
    print(pd_mean)
    