from collections import Counter

from parser import parse_page
from saver import sort_and_save_animals


BASE_URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

def main(url: str) -> None:
    """Parse Wikipedia pages to count an amount of animals and save result to
    a csv file 'beasts.csv'."""

    sort_and_save_animals(animals_count=count_animals(url=url))

def count_animals(url: str) -> Counter:
    """Return a map with amount of animals from Wikipedia divided by letters of
    the alphabet."""

    animals: Counter = Counter()
    page_link: str | None = url
    while page_link:
        one_page_animals, next_page_link = parse_page(page_link)
        # Counter's update method sums values in case of identical keys
        animals.update(one_page_animals)
        page_link = next_page_link
        print(f'Collected {len(animals)} categories', end='\r')
    print('\nParsing completed')
    return animals


if __name__ == '__main__':
    try:
        main(BASE_URL)
    except KeyboardInterrupt:
        print('\nCanceled by user')
