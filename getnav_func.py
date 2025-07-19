import requests
from bs4 import BeautifulSoup

def get_nav(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    nav_amt = soup.select_one('div.leftblok span.amt')
    current_nav = ''

    if nav_amt:
        nav = round(float(nav_amt.text.split()[1]), 2)
        current_nav = nav
    else:
        current_nav = 'Element or amount not found'

    return current_nav