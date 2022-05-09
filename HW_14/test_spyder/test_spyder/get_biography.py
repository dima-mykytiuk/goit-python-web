import sqlite3

import requests
from bs4 import BeautifulSoup

from test_spyder.db.db import db_session
from test_spyder.models import Biography


def get_biography():
    links = []
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_13/test_spyder/quotes.db') as con:
        cur = con.cursor()
        get_links = """
        SELECT DISTINCT(q.link)
        FROM quotes q
        """
        check = cur.execute(get_links)
        for item in check.fetchall():
            for i in item:
                links.append(i)
    for item in links:
        req = requests.get(item)
        soup = BeautifulSoup(req.text, 'lxml')
        name = soup.find('h3', class_='author-title')
        date = soup.find('span', class_='author-born-date')
        location = soup.find('span', class_='author-born-location')
        bio = soup.find('div', class_='author-description')
        bio_to_db = Biography(author=name.text.strip(),
                              birthday=date.text.strip(),
                              born_location=location.text.strip(),
                              biography=bio.text.strip())
        db_session.add(bio_to_db)
        db_session.commit()
get_biography()