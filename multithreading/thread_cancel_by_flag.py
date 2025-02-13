import threading
import time
from typing import List

from multithreading.o1_problem_demo import read_ints

should_stop = False

def count_three_sum(lst: List[int]):
    global should_stop
    print('Start counting three sum')
    n = len(lst)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if should_stop:
                    print('Task was canceled')
                    counter = -1
                    return counter
                if lst[i] + lst[j] + lst[k] == 0:
                    counter += 1
                    print(f'triple found: {lst[i]}, {lst[j]}, {lst[k]}')
    print(f'triple count: {counter}')
    return counter

if __name__ == '__main__':
    print('started main')
    ints = read_ints('1Kints.txt')

    p = threading.Thread(target=count_three_sum, args=(ints,))
    p.start()

    time.sleep(5)

    should_stop = True

    time.sleep(2)

    print('finished main')

