import requests

cookies = {
    '__ddg1_': 'witTuL8RTdrgjRQZO03M',
    # 'session': '60b143784f65b8ff206e7f49183c51dd',
    # 'refresh': '1669524196.4885',
}

headers = {
    'authority': 'sci-hub.se',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'referer': 'https://sci-hub.se/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
for i in range(1000):
    response = requests.get('https://sci-hub.se/10.1016/j.apsb.2021.06.014', cookies=cookies, headers=headers)
    print(response.text)