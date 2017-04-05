# -*- coding: utf-8 -*-
import aiohttp
import asyncio


async def get_webpage(url):
    print("Getting url %s" % url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)


async def print_digit(digit):
    print(str(digit))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(print_digit(1))
    loop.create_task(print_digit(2))
    loop.create_task(get_webpage('http://python.org/'))
    loop.create_task(print_digit(3))
    loop.create_task(print_digit(4))
    loop.run_until_complete(asyncio.sleep(5))
