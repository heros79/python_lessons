import threading
import time

from multithreading.o1_problem_demo import read_ints


class ThreeSumTask:


    def __init__(self, ints):
        self.ints = ints
        self.canceled = False
        self.lock_obj = threading.Lock()


    def run(self):
        self.count_three_sum()


    def cancel(self):
        with self.lock_obj:
            self.canceled = True


    def count_three_sum(self):
        print('Start counting three sum')
        lst = self.ints
        n = len(lst)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.canceled:
                        print('Task canceled')
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
    task = ThreeSumTask(ints)
    p = threading.Thread(target=task.run)
    p.start()

    time.sleep(5)

    task.cancel()

    p.join()

    print('finished main')