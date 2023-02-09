""" Сколько HTML - тегов в коде главной страницы сайта greenatom.ru? 
Сколько из них содержит атрибуты? Напиши скрипт на Python, 
который выводит ответы на вопросы выше """

from bs4 import BeautifulSoup
import requests
import lxml

URL = 'https://greenatom.ru/'


def set_session_header() -> requests.Session():
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en"
        }
    return session


def parse(session: requests.Session, URL: str) -> BeautifulSoup:
    return BeautifulSoup(session.get(URL).text, 'lxml')


def getTagsCount(soup: BeautifulSoup) -> int:
    return len(soup.findAll())


def getTagsWithAttributesCount(soup: BeautifulSoup) -> int:
    return len([tag for tag in soup.findAll() if len(tag.attrs) > 0])


if __name__ == '__main__':
    session = set_session_header()
    soup = parse(session, URL)
    print(f'Количество тегов на странице: {getTagsCount(soup)}')
    print(
        f'Количество тегов с атрибутами на странице: {getTagsWithAttributesCount(soup)}')
