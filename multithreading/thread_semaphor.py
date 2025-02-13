import threading
import concurrent.futures
import time
import random


def work(semaphore):
    time.sleep(random.randint(5, 10))
    print('Release 1 connections')
    semaphore.release()


def connections_guard(semaphore, reached_max_connection):
    while True:
        print(f'[guard] semaphore {semaphore._value}')
        time.sleep(1.5)

        if semaphore._value == 0:
            reached_max_connection().set()
            print(f'[guard] Reached max connections')
            time.sleep(2)
            reached_max_connection().cleare()


def connect(semaphore, reached_max_connection):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            connections_counter = 0
            while not reached_max_connection.is_set():
                print(f'\nConnections n = {connections_counter}')
                semaphore.acquire()
                connections_counter += 1

                executor.submit(work, semaphore)
                time.sleep(0.8)

            time.sleep(5)

if __name__ == '__main__':
    max_connection = 10
    reached_max_connection = threading.Event()

    semaphore = threading.Semaphore(value=max_connection)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(connections_guard, semaphore, reached_max_connection)
        executor.submit(connect, semaphore, reached_max_connection)