from multithreading.decoarators import measure_time


class Foo:

    def __init__(self):
        self.my_num = 0

    @measure_time
    def increment(self):
        for _ in range(0, 10000000):
            self.my_num += 1
        return self.my_num


    @measure_time
    def decrement(self):
        for i in range(0, 10000000):
            self.my_num -= 1
        return self.my_num

    @measure_time
    def increment_data(self, data):
        for _ in range(0, 10000000):
            data += 1
        return data

    @measure_time
    def decrement(self, data):
        for i in range(0, 10000000):
            data -= 1
        return data