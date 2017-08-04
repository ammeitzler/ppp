from bs4 import BeautifulSoup
import requests

endpt = "https://www.facebook.com/angie.meitzler"

page_nums = range(713)[::120]

entry_urls = list()