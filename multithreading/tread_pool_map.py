from multithreading.model import Foo
import concurrent.futures

if __name__ == '__main__':
    print('Started main')

    foo = Foo()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(foo.increment_data, (0, 0))
        for r in result:
            print(f'{r=}')

    print('Finished main')
