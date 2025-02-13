import threading
import time

from multithreading.o1_problem_demo import read_ints

class StopThread(threading.Thread):
    def __init__(self, name):
        super(StopThread, self).__init__(name=name)
        self.stop_event = threading.Event()


    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()


class ThreeSumTaskUnit(StopThread):


    def __init__(self, ints, name='TestThread'):
        super().__init__(name)
        self.ints = ints


    def run(self):
        print(f'{self.name} started')
        self.count_three_sum()
        print(f'{self.name} finished')


    def count_three_sum(self):
        print('Start counting three sum')
        lst = self.ints
        n = len(lst)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.stopped():
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
    task = ThreeSumTaskUnit(ints, 'My thread')
    task.start()

    time.sleep(5)

    task.stop()

    task.join()

    print('finished main')