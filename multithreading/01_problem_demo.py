import sys
from typing import List


def read_ints(path: str):
    lst = []
    with open(path, 'r') as f:
        while line:=f.readline():
            lst.append(int(line))
    return lst

def count_three_sum(lst: List[int]):
    print('Start counting three sum')
    n = len(lst)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if lst[i] + lst[j] + lst[k] == 0:
                    counter += 1
                    print(f'triple found: {lst[i]}, {lst[j]}, {lst[k]}')
    print(f'triple count: {counter}')


if __name__ == '__main__':
    print('Started main')
    lst = read_ints('input.txt')
    count_three_sum(lst)
