import concurrent.futures
import time

from multithreading.model import Foo


def div(divisor, limit):
    print(f'Started {divisor=}')
    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            #print(f'{divisor=}, {x=}')
            time.sleep(0.2)
    print(f'\nFinished {divisor=}', end='\n')
    return result


def before_executor(name):
    print(f'{name=}')


if __name__ == '__main__':
    print(f'Stared main')
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures.append(executor.submit(div, 3, 150))
        futures.append(executor.submit(div, 5, 150))

        while futures[0].running() or futures[1].running():
            print('.', end='')
            time.sleep(0.5)

        for f in futures:
            print(f.result())