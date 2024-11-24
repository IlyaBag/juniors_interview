import unittest
from collections import Counter
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup

from main import count_animals, main
from parser import get_next_page_link


class TestAnimalsCounter(unittest.TestCase):
    """Test the main functionality of the application."""
    def test_main(self):
        """Test receiving and saving the parsing result."""
        with patch('main.count_animals') as mock_count_animals:
            mock_count_animals.return_value = Counter(A=3, B=2, C=1)
            main('https://somesite.com')
            mock_count_animals.assert_called_once()

        expected_result = 'A,3\nB,2\nC,1\n'
        with open('beasts.csv', 'r') as f:
            saved_result = f.read()
        self.assertEqual(saved_result, expected_result)

    @patch('requests.get')
    def test_count_animals(self, mock_get: MagicMock):
        """Test parsing a single page and counting the number of animals."""
        mock_response = MagicMock()
        mock_response.text = """
            <html>
            <body>
              <div id="mw-pages">
                <div class="mw-category-group">
                  <h3>A</h3>
                  <ul>
                    <li>Animal1</li><li>Animal2</li><li>Animal3</li>
                  </ul>
                </div>
                <div class="mw-category-group">
                  <h3>B</h3>
                  <ul>
                    <li>Beast1</li><li>Beast2</li>
                  </ul>
                </div>
                <div class="mw-category-group">
                  <h3>C</h3>
                  <ul>
                    <li>Creature1</li>
                  </ul>
                </div>
              </div>
            </body>
            </html>
        """
        mock_get.return_value = mock_response
        result = count_animals('https://somesite.com')
        expected_result = Counter(A=3, B=2, C=1)
        self.assertEqual(result, expected_result)

    def test_get_next_page_link(self):
        """Test finding the link to the next page."""
        html = """
            <div>
              <a href="/next-page">Следующая страница</a>
            </div>
        """
        soup = BeautifulSoup(html, features='html.parser')
        tag = soup.div
        result = get_next_page_link(tag=tag)
        expected_result = 'https://ru.wikipedia.org/next-page'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
