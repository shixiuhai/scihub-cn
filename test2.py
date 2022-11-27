import requests
# 导入线程池
from concurrent.futures import ThreadPoolExecutor
# 创建一个5个线程的消费
import time
# 定义可以同时执行的函数数量
threadPool = ThreadPoolExecutor(max_workers=5) 
import requests


cookies = {
    '__ddg1_': 'aSECdDE8UlexbXF4J8UB',
    'session': 'c6abbd37fafb32bb1e280e0de8553c11',
    'refresh': '1669532305.7575',
}

headers = {
    'authority': 'sci-hub.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

proxies={'http': 'socks://127.0.0.1:10808','https': 'socks://127.0.0.1:10808'}
def aa():
    print('++')
    response = requests.get('https://www.sci-hub.ru/10.1109/ACC.1999.786344', cookies=cookies, headers=headers,allow_redirects=True,proxies=None)
    print('--')
    
    print(response.url)
    response.encoding = 'utf-8'
    print(response.text)

for i in range(10000):
    threadPool.submit(aa)
    break
