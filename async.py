import asyncio
import time

async def say_after(delay, what):
    print(what)
    await asyncio.sleep(delay)
    

async def main():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(1,"Hello"))
    task2 = asyncio.create_task(say_after(2,"World"))
    await task1 # Wait here until finish this task
    print("Running... 1")
    #await say_after(1, 'hello')
    #await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())
print("Running... 2")
