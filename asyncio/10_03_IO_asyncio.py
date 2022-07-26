import asyncio
import os

import aiohttp

from multithreading.decorators import async_measure_time


async def download_site(url, session):
    async with session.get(url) as response:
        print(f'Read {response.content.total_bytes} from {url}')


@async_measure_time
async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(url, session))
            tasks.append(task)

        try:
            print('before await')
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as ex:
            print(repr(ex))


if __name__ == '__main__':
    sites = [
                "https://forexvideourok.ru/category/literature/",
                "https://book.mql4.com/ru/practice"
            ] * 80

    asyncio.run(download_all_sites(sites))
