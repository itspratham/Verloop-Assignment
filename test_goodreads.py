import unittest
from goodreads import GoodreadsAPIClient

class TestSum(unittest.TestCase):
    obj = GoodreadsAPIClient()

    def test_hyphen_books(self):
        self.assertEqual(self.obj.get_book_details("https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire"), {'title': 'A Song of Ice and Fire (A Song of Ice and Fire, #1-5)', 'average_rating': '4.58', 'num_pages': '5216', 'image_url': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1339340118l/12177850._SX98_.jpg', 'publication_year': '2011', 'ratings_count': '27530', 'authors': 'George R.R. Martin'}, "Should be somethingelse")

    def test_dot_books(self):
        self.assertEqual(self.obj.get_book_details("https://www.goodreads.com/book/show/12067.Good_Omens"),{'title': 'Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch', 'average_rating': '4.24', 'num_pages': '491', 'image_url': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1392528568l/12067._SY160_.jpg', 'publication_year': '2006', 'ratings_count': '468882', 'authors': 'Terry Pratchett, Neil Gaiman'},"Should be something else")

    def test_error(self):
        self.assertEqual(self.obj.get_book_details("https://www.gooreads.com/book/show/22034.The_Godfather"),"InvalidGoodreadsURL", "Something else")

if __name__ == '__main__':
    unittest.main()