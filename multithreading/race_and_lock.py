import concurrent.futures
import threading
import time


class BankAccount:

    def __init__(self):
        self.balance = 100
        self.lock_obj = threading.Lock()


    def update_balance(self, transaction, amount):
        print(f'{transaction} started')
        with self.lock_obj:
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount

        print(f'{transaction} completed')


if __name__ == '__main__':
    acc = BankAccount()
    print(f'Main started, account balance: {acc.balance}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update_balance, ('refill', 'withdraw'), (100, -200))

    print(f'Main finished. Balance: {acc.balance}')
# if __name__ == '__main__':
#     lock_obj = threading.Lock()
#     print(lock_obj.locked())
#     lock_obj.acquire()
#     print(lock_obj.locked())
#     lock_obj.release()
#     print(lock_obj.locked())


