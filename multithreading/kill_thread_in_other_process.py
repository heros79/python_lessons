import multiprocessing
import time

from multithreading.o1_problem_demo import count_three_sum
from o1_problem_demo import read_ints

if __name__ == '__main__':
    print('started main')
    ints = read_ints('1Kints.txt')

    p = multiprocessing.Process(target=count_three_sum, args=(ints,))
    p.start()

    time.sleep(5)


    p.terminate()

    print('finished main')