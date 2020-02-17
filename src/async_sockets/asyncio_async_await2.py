import requests
from random import randrange
from time import time




def get_file(url):
    req = requests.get(url, allow_redirects=True)
    return req


def write_file(response):

    filename = response.url.split('/')[-1] + str(randrange(100))
    print(filename)
    with open(filename, "wb") as file:
        file.write(response.content)


def main():
    t0 = time()
    url = "https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


# if __name__ == "__main__":
#     main()
#################################################################################


import asyncio
import aiohttp


def write_image(data):
    filename = "file-{}.jpeg".format(int(time() * 1000))
    with open(filename, "wb") as file:
        file.write(data)

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main2():
    url = "https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)
