from threading import Thread

from multithreading.model import Foo

my_num = 0

foo = Foo()


a = Thread(target=foo.increment)
b = Thread(target=foo.decrement)

a.start()
b.start()
a.join()
b.join()

print(foo.my_num)

foo.increment()
foo.decrement()


print(foo.my_num)