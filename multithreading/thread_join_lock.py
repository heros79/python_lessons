import time
from threading import Thread


def foo():
    print('Running first thread\n')
    print('foo join bar\n')
    time.sleep(2)
    t2.join()

    print('foo sleep')
    time.sleep(5)
    print('end of foo')

def bar():
    print('Running second thread\n')
    print('bar join foo\n')
    time.sleep(2)
    t1.join()

    print('bar sleep')
    time.sleep(5)
    print('end of bar')


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.start()
    t2.start()