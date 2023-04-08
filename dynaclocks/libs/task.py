import asyncio

class Task:
    scheduled = []
    asyncio = asyncio

    @staticmethod
    def spawn(function):
        Task.scheduled.append(function)

    @staticmethod
    async def wait(time:float):
        await asyncio.sleep(time)