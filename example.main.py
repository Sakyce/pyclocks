from dynaclocks import *

workspace = GetService(Workspace)

Settings.WindowSize = Vector2(500,800)

for i in range(6):
    part = Part()
    part.Position = Vector2.RandomBetween(0,0,*Settings.WindowSize)
    part.Size = Vector2(100,50)
    part.Parent = workspace

PrintTree()
Run()