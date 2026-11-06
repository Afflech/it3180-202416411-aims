import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def test_search_by_title(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual([items[0]], search_by_title(items, "Lion"))

    def test_search_by_title_ignores_case(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual([items[0]], search_by_title(items, "lion"))


if __name__ == "__main__":
    unittest.main()
