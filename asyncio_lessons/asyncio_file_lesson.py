import asyncio

import aiofiles

from multithreading.decoarators import measure_time, async_measure_time


def read_large_file():
    with open('big_file.txt','r') as f:
        return f.read()


async def read_large_file_async():
    async with aiofiles.open('big_file.txt','r') as f:
        return await f.read()


def count_words(text: str):
    return len(text.split(' '))

@async_measure_time
async def async_main():
    text = await read_large_file_async()
    print(count_words(text))


@measure_time
def main():
    text = read_large_file()
    print(count_words(text))


if __name__ == '__main__':
    asyncio.run(async_main())
    main()

