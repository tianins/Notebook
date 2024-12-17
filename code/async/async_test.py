import asyncio
import time
from loguru import logger
count_list = []
async def count_async(idx,sleep_time):
    print("One")
    await asyncio.sleep(sleep_time)
    
    print("Two")
    return idx,sleep_time

def count():
    print("One")
    time.sleep(1)
    print("Two") 

async def main_async():
    logger.info("start")
    # await asyncio.gather(count_async(1,3), count_async(2,1), count_async(3,2))
    task = []
    task.append(count_async(1,3))
    task.append(count_async(2,1))
    task.append(count_async(3,2))
    results = await asyncio.gather(*task)
    for index, result in sorted(results, key=lambda x: x[0]):
        count_list.append([index,result])
    logger.info("end")

def main():
    logger.info("start")
    for _ in range(3):
        count()
    logger.info("end")
    
async def main_test():
    print(f"started at {time.strftime('%X')}")

    await count_async()
    #await say_after(1, 'hello')执行完之后，才继续向下执行
    await count_async()
    await count_async()
    print(f"finished at {time.strftime('%X')}")


# main()
asyncio.run(main_async())
print(count_list)