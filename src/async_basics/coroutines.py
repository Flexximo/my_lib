import asyncio
import time

async def turn_wait():
    await asyncio.sleep(100000)
    print((2+3j)**3)

async def main():
    try:
        await asyncio.wait_for(turn_wait(), timeout=1.0)
    except asyncio.TimeoutError:
        print("timeout!")
        print((2+3j)**3)
asyncio.run(main())
