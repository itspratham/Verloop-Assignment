# # key: ViJN85HEI2MUhkH0Tb0xIg
# # secret: aF7xy0jEx8E7QWxIpxdYqNlcJBqhVwYWCmQEGiY56Pk
# I have crested my own developer key here in goodread.com
import requests
from xml.etree import ElementTree

class GoodreadsAPIClient:
    def get_book_details(self,url):
        from requests.exceptions import ConnectionError
        try:
            requests.get(url,timeout = 5)
        except ConnectionError:
            return "InvalidGoodreadsURL"
        dictionary = {}
        url = url.split("/")
        if "-" in url[-1]:
            f = url[-1].split("-")
        if "." in url[-1]:
            f = url[-1].split(".")
        f = "https://www.goodreads.com/book/show/{}.xml?key=ViJN85HEI2MUhkH0Tb0xIg".format(f[0])
        k = requests.get(f)
        cont = k.content
        cont_String = cont.decode("utf-8")
        h = ElementTree.fromstring(cont_String)
        cou = h.findall('book')
        for cou in cou:
            dictionary["title"] = cou.find('title').text
            dictionary["average_rating"] = cou.find('average_rating').text
            dictionary["num_pages"] = cou.find('num_pages').text
            dictionary["image_url"] = cou.find('image_url').text
            dictionary["publication_year"] = cou.find('publication_year').text
            dictionary["ratings_count"] = cou.find('ratings_count').text
            b = [i.text for i in cou.findall('authors/author/name')]
            dictionary["authors"] = ', '.join(b)
        return dictionary

# url = input("Enter the url: ")
# obj = GoodreadsAPIClient()
# print(obj.get_book_details(url))