from dataclasses import dataclass
from typing import List
from urllib.parse import urljoin
import requests
import requests_html

#
user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#
# resp = requests.get(
#     "https://www.delivery-club.ru/srv/FARSh/#Bulvar_Entuziastov2/",
#     headers=user_agent,
# )


@dataclass
class Product:
    name: str = ""
    description: str = "отсутсвует"
    product_id: str = 0
    quantity: int = 0
    img_url: str = ""


def base_url(url):
    return ""


def parse(url: str) -> List[Product]:
    # with open("/Users/denis.fetinin/PycharmProjects/FeedMe/feed_me/order/stubs/farsh.html", 'rb') as fh:
    #     content = fh.read()
    r = requests_html.HTMLSession()

    html = r.get(url, headers=user_agent,).html
    products = []
    for product_html in html.find(".dish_list > li"):
        product = Product()
        product.name = product_html.find(".product_title")[0].text
        if product_html.find("p[itemprop]"):
            product.description = product_html.find("p[itemprop]")[0].text

        img_html = product_html.find('img')[0]
        img_url = img_html.attrs.get("data-load", "") or img_html.attrs.get("src", "")
        product.img_url = urljoin("https://www.delivery-club.ru", img_url)

        for f in product_html.find("form > p > input[type=hidden]"):
            if f.attrs["name"] == "product_id":
                product.product_id = int(f.attrs["value"])
            elif f.attrs["name"] == "quantity":
                product.quantity = f.attrs["value"]

        products.append(product)

    return products

if __name__ == '__main__':
    print(parse("https://www.delivery-club.ru/srv/FARSh/#Bulvar_Entuziastov2/"))

