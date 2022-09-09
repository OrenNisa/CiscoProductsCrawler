import json
import requests
from bs4 import BeautifulSoup

from product import Product


def main():
    cisco_soup = soup_getter('https://www.cisco.com/c/en/us/support/all-products.html')

    data = cisco_soup.find_all('tr')[1]  # get the second line of main table
    categories = data.find_all('li')
    for category in categories:
        link = category.find('a')['href']  # takes all links
        link = link if link.startswith('http') else ('https:' + link)  # add https to link
        search_in_category(link)


def search_in_category(link):
    category_soup = soup_getter(link)

    category_name = category_soup.find('h1', id='fw-pagetitle').text.strip()  # search category by element id
    data = category_soup.find_all('li')
    for row in data:
        link_in_page = row.find('a')
        if link_in_page is not None:  # continue only if there is a link
            link_in_page = link_in_page['href']
            if 'cisco.com/c/en/us/support/' in link_in_page:  # continue only if it is product link (this prefix is only for products)
                product_link = link_in_page if link_in_page.startswith('https') else ('https:' + link_in_page)
                search_in_product(category_name, product_link)


def search_in_product(category, link):
    product_soup = soup_getter(link)

    data = product_soup.find('table', class_='birth-cert-table')
    product_obj = Product()
    if data is not None:
        product_obj._vendor = link
        product_obj._url = link
        product_obj._model = product_soup.find('h1', id='fw-pagetitle').text.strip()
        path = path_builder(product_soup, product_obj.getmodel)
        product_obj._path = path
        product_obj._category = category
        specs = data.find_all('tr')
        # run on all specs and checks in "insert_to_product_object" function if it should be saved
        # according to exercise demands.
        for full_spec in specs:
            if full_spec.find('th') is not None:
                spec = full_spec.find('th').text.strip()
                spec_content = full_spec.find('td').find(text=True).strip()
                insert_to_product_object(product_obj, spec, spec_content)
        print(json.dumps(product_obj.__dict__))  # printing to console for tests purpose


def path_builder(soup, product_name):
    path = ""
    all_paths = soup.find_all('span', itemprop='name')
    for path_part in all_paths:
        path_part = path_part.text
        path += '/' + path_part
    path += '/' + product_name
    return path


def insert_to_product_object(product_obj, spec, spec_content):
    if is_necessary_spec(spec):
        match spec:
            case 'Series':
                product_obj._series = spec_content
            case 'Release Date':
                product_obj._release = spec_content
            case 'Series Release Date':
                product_obj._release = spec_content
            case 'End-of-Sale Date':
                product_obj._endofsale = spec_content
            case 'End-of-Support Date':
                product_obj._enfodsupport = spec_content


relevantSpecs = ['Series', 'Series Release Date', 'End-of-Sale Date', 'End-of-Support Date']


def is_necessary_spec(spec):
    for relevant_spec in relevantSpecs:
        if spec in relevant_spec:
            return True
    return False


def soup_getter(link):
    html = requests.get(link).text
    return BeautifulSoup(html, 'lxml')


if __name__ == "__main__":
    main()
