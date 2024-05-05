from PySide6.QtWidgets import QApplication

from Window import Window

app = QApplication()

window = Window()
window.show()
app.exec()

# async def prprint():
#     for i in range(10):
#         print(i)
#
# async def prprint2():
#     for i in range(10, 20):
#         print(i)
#
# await prprint()
# await prprint2()

# import asyncio
# from datetime import datetime
#
#
# async def prprint():
#     filr = open('log.txt', 'w')
#     start = datetime.now()
#     for i in range(8000000000):
#         print(i, file=filr)
#     filr.close()
#     end = datetime.now()
#
#
# async def prprint2():
#     for i in range(10, 2000):
#         print(i)
#
# async def main():
#     await prprint()
#     await prprint2()
#
# if __name__ == "__main__":
#     asyncio.run(main())


#
# import asyncio
#
# file = open('log.txt', 'w')
# async def task1():
#     print("Task 1 started")
#     for i in range(10000000):
#         print(i, file=file)
#     # await asyncio.sleep(1)
#     print("Task 1 completed")
#     return "Result 1"
#
# async def task2():
#     print("Task 2 started")
#     for i in range(1000000):
#         print(i)
#     # await asyncio.sleep(2)
#     print("Task 2 completed")
#     return "Result 2"
#
# async def main():
#     results = await asyncio.gather(task1(), task2())
#     print("All tasks completed")
#     print("Results:", results)
#
# asyncio.run(main())
# file.close()