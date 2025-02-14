import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print('Loop is running')



async def main():
    await_obj = asyncio.gather(tick(), tick(), tick())
    for i in asyncio.all_tasks():
        print(i, end='\n')
    await await_obj


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
        #loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('Manually close program')
    finally:
        loop.close()