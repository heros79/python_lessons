import random
import threading
import time
from datetime import datetime


class HorseRace:
    def __init__(self):
        self.barrier = threading.Barrier(4)
        self.horses = ['Artax', 'Frankel', 'Bucephalus', 'Barton']


    def lead(self):
        horse = self.horses.pop()
        time.sleep(random.randint(1, 5))
        print(f'\n{horse} reached the barrier at: {datetime.now()}')
        self.barrier.wait()

        time.sleep(random.randint(1, 5))
        print(f'\n{horse} started at {datetime.now()}')

        time.sleep(random.randint(1, 5))
        print(f'\n{horse} finished at {datetime.now()}')

        self.barrier.wait()
        print('Race finished')


if __name__ == '__main__':
    print('Race preparation')
    race = HorseRace()
    for i in range(4):
        thread = threading.Thread(target=race.lead)
        thread.start()

