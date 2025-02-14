import concurrent.futures
import time


def div(divisor, limit):
    print(f'started div = {divisor}')

    result = 0
    for i in range(1, limit):
        if i % divisor == 0:
            result += i
            print(f'{divisor=}, {i=}')
        time.sleep(0.2)

    print('Raise exception')
    raise Exception('bad things happen!')


# if __name__ == '__main__':
#     print('Main startded')
#     with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
#         future = executor.submit(div, 3, 15)
#         time.sleep(5)
#         print('Nothings happen until....')
#
#         try:
#             res = future.result()
#         except Exception as e:
#             print(e)
#     print('Main finished')

if __name__ == '__main__':
    print('Main startded')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        res_list = executor.map(div, (3, 5,), (15, 25))
        time.sleep(5)
        print('Nothings happen until....')

        try:
            while res_list:
                cur_res = res_list.__next__()
        except StopIteration:
            pass
        except Exception as e:
            print(e)
    print('Main finished')
