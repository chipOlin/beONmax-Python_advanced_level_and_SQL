import requests as requests

from multithreading.decorators import measure_time


def download_site(url, session):
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')


@measure_time
def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == '__main__':
    sites = [
        "https://forexvideourok.ru/category/literature/",
        "https://book.mql4.com/ru/practice"
    ] * 80

    download_all_sites(sites)
