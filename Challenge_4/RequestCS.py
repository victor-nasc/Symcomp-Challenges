import requests
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='RequestCS',
        description='Make requests given a url'
    )
    parser.add_argument('url', type=str, help='Url to make requests')

    args = parser.parse_args()
    url = args.url

    headers = {
        'User-Agent': 'RequestCS/1.0 (https://github.com/senshiacy; contact via GitHub Issues)'
    }
    r = requests.get(url, headers=headers)
    print(r.text)
    exit(0)
    j = r.json()
    with open("CS.json", "w+", encoding='utf-8') as f:
        json.dump(j, f, ensure_ascii=False, indent=4)
