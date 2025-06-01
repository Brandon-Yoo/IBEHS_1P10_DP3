from typing import List


class RollingAverage:
    @staticmethod
    def calculate(values: List[int], window_average: int)->int:
        while True:
            if len(values) == window_average:
                average = round(sum(values) / len(values), 2)
                break
            elif len(values) > window_average:
                values.pop(0) 
            else:
                average = None
                break
        return average