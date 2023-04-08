class Task:
    scheduled = []

    @staticmethod
    def spawn(function):
        async def coro():
            pass
        Task.scheduled.append(coro())
        return coro

    @staticmethod
    def wait(time:float):
        pass