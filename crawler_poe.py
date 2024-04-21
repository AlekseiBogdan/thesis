import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

def poe_scrape():
    base_url = 'https://ru.pathofexile.com/forum/view-thread/2411128/page/'

    messages = []
    for i in range(1, 11):
        url = f'{base_url}{i}'
        response = requests.get(url,  headers=headers)
        print(f"scraping {url}")
        if response.status_code != 200:
            print("Error fetching page")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        
        content = soup.find_all('tr')
        for row in content:
            for message in row.select('div.content'):
                messages.append([message.get_text()])

    return messages

def d2ru_scrape():
    base_url = ['https://dota2.ru/forum/threads/vyshel-patch-7-35.1561261/page-', 'https://dota2.ru/forum/threads/v-cs-2-net-nagruzki-i-nizkaja-moschnost-gp.1553019/page-', 'https://dota2.ru/forum/threads/vam-po-kajfu-kazhduju-igru-igrat-na-mirazhe.1550725/page-', 'https://dota2.ru/forum/threads/1000-rejtinga.1553352/page-']

    messages = []
    for thread_url in base_url:
        for i in range(1, 11):
            url = f'{thread_url}{i}'
            response = requests.get(url,  headers=headers)
            print(f"scraping {url}")
            if response.status_code != 200:
                print("Error fetching page")
                continue

            soup = BeautifulSoup(response.content, 'html.parser')

            
            content = soup.find_all('div', class_='forum-theme__item-block-mess')
            print(content)
            for row in content:
                messages.append([row.get_text()])

    return messages

def gamedev_scrape():
    base_url = 'https://gamedev.ru/gamedesign/forum/?id=276346&page='

    messages = []
    for i in range(1, 11):
        url = f'{base_url}{i}'
        response = requests.get(url,  headers=headers)
        print(f"scraping {url}")
        if response.status_code != 200:
            print("Error fetching page")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        
        content = soup.find_all('div', class_='bound overflow')
        print(content)
        for row in content:
            messages.append([row.get_text()])

    return messages

def main():
    messages = []
    messages_poe = poe_scrape()
    messages_d2ru = d2ru_scrape()
    messages_gamedev = gamedev_scrape()

    messages.extend(messages_poe)
    messages.extend(messages_d2ru)
    messages.extend(messages_gamedev)

    df = pd.DataFrame(messages, columns=['Messages'])

    df.to_csv('messages.csv', encoding='utf-8-sig', index=False)

if __name__ == '__main__':
    main()