import requests
import io
# 导入线程池
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
import queue
# 重新封装线程池类
class ThreadPoolExecutor(ThreadPoolExecutor):
    """
    重写线程池修改队列数
    """
    def __init__(self, max_workers=None, thread_name_prefix=''):
        super().__init__(max_workers, thread_name_prefix)
        # 队列大小为最大线程数的两倍
        self._work_queue = queue.Queue(self._max_workers * 2)
# 创建一个5个线程的消费
import random
# 定义可以同时执行的函数数量
threadPool = ThreadPoolExecutor(max_workers=5) 
def down():
    response = requests.get('https://zero.sci-hub.se/6510/1d5292d9ce85c525ad909da9f5040bec/huang2017.pdf')
    bytes_io = io.BytesIO(response.content)  # 转换为字节流
    print("成功")
    with open('files/%s.pdf'%(str(random.randint(1,100000))), 'wb') as file:
        file.write(bytes_io.getvalue())  # 保存到本地
        print("保存成功")
# down()
taskList=[]
for i in range(1000):
    task=threadPool.submit(down)
    taskList.append(task)
# 等待所有完成
wait(taskList, return_when=ALL_COMPLETED)
