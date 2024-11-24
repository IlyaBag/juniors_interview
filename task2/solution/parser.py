import requests
from bs4 import BeautifulSoup, Tag

from exceptions import ParserException


def parse_page(url: str) -> tuple[dict[str, int], str | None]:
    """Parse Wikipedia web page given by 'url' parameter.
    Return tuple of two elements:
    - dict witch keys are the first letters of animals names and values are
      their amount
    - string with a link to a next page to parse
    """

    resp = requests.get(url=url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, features='html.parser')
    target_tag_id = 'mw-pages'
    target_tag = soup.find(id=target_tag_id)
    if type(target_tag) is not Tag:
        raise ParserException(
            f'Can\'t find an HTML tag with id="{target_tag_id}"'
        )

    one_page_animals = get_animals_from_page(target_tag)
    next_page_link = get_next_page_link(target_tag)

    return one_page_animals, next_page_link

def get_animals_from_page(tag: Tag) -> dict[str, int]:
    """Returns a map with the first letter of the names and the number of
    animals in the given HTML block."""

    categories = tag.find_all(class_='mw-category-group')
    animals_count = {}
    for cat in categories:
        animals_count[cat.h3.string] = len(cat.find_all('li'))
    return animals_count

def get_next_page_link(tag: Tag) -> str | None:
    """Find the link to the next page in the given HTML block."""
    next_page = tag.find('a', string='Следующая страница')
    next_page_link = None
    if type(next_page) is Tag:
        next_page_link = f'https://ru.wikipedia.org{next_page.get('href')}'
    return next_page_link
