import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    result = nums.astype(object)
    result[(nums % 3 == 0) & (nums % 5 != 0)] = 'fizz'
    result[(nums % 5 == 0) & (nums % 3 != 0)] = 'buzz'
    result[(nums % 15 == 0)] = 'fizzbuzz'
    return result
