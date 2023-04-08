import asyncio
from dynaclocks import *

Settings.WindowSize = Vector2(500,500)


frame = Frame()
frame.Position = UDim2.fromScale(0.5,0.5)
frame.Size = UDim2.fromScale(0.1,0.1)
frame.Color = Color3(0,0,1)
frame.Parent = GetService(Workspace)

for i in range(6):
    part = Part()
    part.Position = Vector2.RandomBetween(0,0,*Settings.WindowSize)
    part.Size = Vector2(100,50)
    part.Color = Color3(1,0,0)
    part.Parent = GetService(Workspace)

@Task.spawn
async def t():
    s = 0
    while True:
        s += 1
        frame.Position = UDim2.fromScale(
            math.sin(s)*0.1,
            math.cos(s)*0.1
        )
        await asyncio.sleep(0.01)

PrintTree()
Run()