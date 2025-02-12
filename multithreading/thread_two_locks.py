import threading
import time

a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()

def thread_one():
    global a
    global b

    print('thread_one acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    print('thread_one acquired lock b')
    b_lock.acquire()
    time.sleep(5)

    a += 5
    b += 5

    print('thread_one released both locks')
    a_lock.release()
    b_lock.release()


def thread_two():
    global a
    global b

    print('thread_two acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    print('thread_two acquired lock a')
    a_lock.acquire()
    time.sleep(5)

    a += 10
    b += 10

    print('thread_two released both locks')
    b_lock.release()
    a_lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=thread_one)
    t1.start()
    t2 = threading.Thread(target=thread_two)
    t2.start()