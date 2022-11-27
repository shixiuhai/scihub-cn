import asyncio
from scihub_cn.scihub import SciHub

def fetch_by_doi(dois: list, destination: str):
    """
    根据 doi 获取文档
    Args:
        dois: 文献DOI号列表
        path: 存储文件夹
    """

    sh = SciHub()
    loop = asyncio.get_event_loop()
    # 获取所有需要下载的scihub直链
    tasks = [sh.async_get_direct_url(doi) for doi in dois]
    all_direct_urls = loop.run_until_complete(asyncio.gather(*tasks))
    print(all_direct_urls)
    # # 下载所有论文
    # loop.run_until_complete(sh.async_download(loop,all_direct_urls, destination=destination))
    # loop.close()

if __name__ == '__main__':
    aList=[]
    for i in range(100000):
        aList.append("10.1038/s41524-017-0032-0")
    fetch_by_doi(aList, f"files/")