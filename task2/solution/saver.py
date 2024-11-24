import csv
from collections import Counter


def sort_and_save_animals(animals_count: Counter) -> None:
    """Make a sorted list of animals count from a given Counter object and save
    it to a csv file."""

    sorted_animals_count_list = sort_animals(animals_count)
    save_amimals_count(sorted_animals_count_list)

def save_amimals_count(animals_count: list[list[str]]) -> None:
    """Save data to a csv file 'beasts.csv'."""
    with open('beasts.csv', 'w') as f:
        csvout = csv.writer(f)
        csvout.writerows(animals_count)

def sort_animals(animals: Counter) -> list[list[str]]:
    """Recieve a mapping object with name's first letters and amount of animals.
    Sort and return a list of lists with pairs of letters and amount."""

    animals_list = [[k, str(v)] for k, v in animals.items()]
    return sorted(animals_list)
