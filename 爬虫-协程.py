import asyncio
import  time

async def fun1():
    print("111")
    await asyncio.sleep(3)
    print("111")

async def fun2():
    print("222")
    await asyncio.sleep(2)
    print("222")

async def fun3():
    print("333")
    await asyncio.sleep(4)
    print("333")

async def main():
    tasks = {
        fun1(),
        fun2(),
        fun3()
    }
    await asyncio.wait(tasks)

if __name__ == '__main__':
    start = time.time();
    asyncio.run(main())
    print(time.time()-start)
    # asyncio.run(fun1())