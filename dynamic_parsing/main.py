import requests
from bs4 import BeautifulSoup
import fake_useragent


def scrap_master(url):

    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}

    req = requests.get(url, headers=header)

    with open('temp_index.html', 'w', encoding='utf-8') as file:
        file.write(req.text)

    with open('temp_index.html', encoding='utf-8') as file:
        source = file.read()

    soup = BeautifulSoup(source, 'lxml')

    all_product = soup.find_all('div', class_='x-product-card-description')
    print(all_product)


scrap_master('https://www.lamoda.ru/c/832/default-sports-men/?multigender_page=1&q=%D0%B4%D0%B6%D0%B8%D0%BD%D1%81%D1%8B&submit=y')