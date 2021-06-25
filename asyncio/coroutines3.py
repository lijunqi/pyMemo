import asyncio
import time

# The asyncio.create_task() function to run coroutines concurrently
# as asyncio Tasks.
async def say_after(delay, what):
    print(delay, what, time.strftime('%X'))
    await asyncio.sleep(delay)
    print(what)

async def main():
    # "Tasks" are used to schedule coroutines concurrently.
    # When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"======  Begin sleep {time.strftime('%X')}")
    await asyncio.sleep(3)
    print(f"======  After sleep {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task2
    print('======  Here call await.')
    await task1

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())