import random
from functools import wraps
import time


# 交换列表中两个元素的位置
def swap(arr: [int], idx: int, idy: int) -> None:
    tmp = arr[idx]
    arr[idx] = arr[idy]
    arr[idy] = tmp


# 生成随机数组
def generate_random_list(lower, upper, size, seed=18) -> [int]:
    random.seed(seed)
    return [random.randint(lower, upper) for _ in range(size)]


# 用于测算时间的修饰器
def exectime(func):
    @wraps(func)
    def time_it(*args, **kwargs):
        start = time.time() * 1000
        try:
            return func(*args, **kwargs)
        finally:
            execution_time = time.time() * 1000 - start
            print("{} execution time: {} ms".format(func.__name__, execution_time))
    return time_it


# 检测一个array是否sorted, 默认检测升序
def is_sorted(arr: [int], asc=True) -> bool:
    for idx in range(1, len(arr)):
        if asc:
            if arr[idx] < arr[idx - 1]:
                return False
        else:
            if arr[idx] > arr[idx - 1]:
                return False
    return True

