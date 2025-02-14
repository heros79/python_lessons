import threading
import time

throw = False

def count():
    i = 0
    while True:
        if throw:
            raise ZeroDivisionError

        i += 1
        print(f'{i=}')
        time.sleep(1)


if __name__ == '__main__':
    print('started main')

    t = threading.Thread(target=count)
    t.start()

    time.sleep(3)

    throw = True

    print('main finished')