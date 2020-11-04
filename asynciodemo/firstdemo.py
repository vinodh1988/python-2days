import asyncio
import time
#asynchronous code - non blocking
async def say_after(delay, task,parameter):
    print(task)
    await asyncio.sleep(delay)
    print(parameter)

async def do_this(task):
    print(task)
    await asyncio.sleep(1)
    print('Done with do this')

async def main():
    print(f"started at {time.strftime('%X')}")

    await asyncio.gather(say_after(1, 'one' ,'message one'),do_this('third task'),say_after(1, 'two' , 'message two'))

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

   