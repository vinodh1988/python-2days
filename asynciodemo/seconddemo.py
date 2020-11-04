import asyncio
import time

async def say_after(delay, task,what):
    print(task)
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'one' ,'message one')
    await say_after(2, 'two' , 'message two')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# await waits for a function which is usually returning Future object 