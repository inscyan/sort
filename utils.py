"""工具类"""

import time
import random
import functools


def generate_partially_ordered_arr(num=100000, reverse_num=10):
    """
    产生部分有序的整数数组（部分有序的定义可参考书上第158页）
    :param num: 数组大小
    :param reverse_num: 倒置对数
    :return:
    """
    arr = list(range(num))
    for lo in random.sample(range(num), reverse_num):
        interval = random.choice(range(1, num))
        hi = min(lo + interval, num - 1)
        arr[hi], arr[lo] = arr[lo], arr[hi]

    return arr


def generate_lot_repeat_arr(num=100000, lower=-10, upper=10):
    """
    产生包含大量重复元素的整数数组
    :param num: 数组大小
    :param lower: 数组元素下界（含）
    :param upper: 数组元素上界（含）
    :return:
    """

    return [random.randint(lower, upper) for _ in range(num)]


def generate_random_arr(num=100000, lower=-50000, upper=50000):
    """
    产生随机整数数组
    :param num: 数组大小
    :param lower: 数组元素下界（含）
    :param upper: 数组元素上界（含）
    :return:
    """

    return [random.randint(lower, upper) for _ in range(num)]


def time_used(unit='s'):
    """
    测定函数执行用时的装饰器
    :param unit: 耗时单位，默认为s(秒)，其余可选参数：m(分)、h(时)
    :return:
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            time_start = time.time()

            # 执行函数
            func_result = func(*args, **kw)

            usetime = time.time() - time_start
            if unit == 'm':
                usetime = usetime / 60
            elif unit == 'h':
                usetime = usetime / 3600
            print('`%s` func time used: %.2f%s' % (func.__name__, usetime, unit))
            return func_result

        return wrapper

    return decorator


def reverse(arr, start, end):
    """
    实现数组逆序，可指定起止索引
    :param arr:
    :param start:
    :param end:
    :return:
    """
    while start < end:
        arr[end], arr[start] = arr[start], arr[end]
        start += 1
        end -= 1


if __name__ == '__main__':
    print(generate_partially_ordered_arr())
    print(generate_lot_repeat_arr())
    print(generate_random_arr())
