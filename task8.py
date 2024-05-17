from typing import Union, List, Tuple
import numpy as np


class Statistics:
    def __init__(self, data: Union[List[int|float], Tuple[int|float], np.ndarray[int|float]]):

        self.data = data
        

    def calculate_mean(self) -> float | int:
        return np.mean(self.data)
        

    def calculate_median(self) -> float | int:
        return np.median(self.data)


    def calculate_mode(self) -> float | int:
        cnts = {}
        keys = []
        for i in set(self.data):
            cnts[i] = list(self.data).count(i)
        for k, v in cnts.items():
            if v == max(cnts.values()):
                keys.append(k)
        return max(keys)
    

    def std(self) -> float | int:
        return np.std(self.data)
    

    def iqr(self) -> float | int:
        q3, q1 = np.percentile(self.data, [75 ,25])
        return q3 - q1

data = [-1, -2, -3, 0, 1, 1, 1, 2, 3, 3, 3, 5, 6]

sample = Statistics(data)

print('Среднее:', sample.calculate_mean())
print('Медиана:', sample.calculate_median())
print('Мода:', sample.calculate_mode())
print('Стандартное отклонение:', sample.std())
print('Интерквартильный размах:', sample.iqr())