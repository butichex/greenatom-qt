""" Напиши функцию на Python, которая возвращает 
текущий публичный IP-адрес компьютера 
(например, с использованием сервиса ifconfig.me) """

from bs4 import BeautifulSoup
import requests
import lxml

URL = 'https://ifconfig.me/'


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


def getIp(soup: BeautifulSoup) -> int:
    return soup.find('strong', attrs={'id': 'ip_address'}).text


if __name__ == '__main__':
    session = set_session_header()
    soup = parse(session, URL)
    print(f'Текущий публичный IP-адрес компьютера: {getIp(soup)}')
