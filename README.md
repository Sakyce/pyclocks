# Clocks : A PyGame Framework inspired by Roblox
### Still a work in progress


## Very simple to use
```py
from dynaclocks import *

# Create 6 Parts with a randomized position
for i in range(6):
    part = Part()
    part.Position = Vector2.RandomBetween(0,0,*Settings.WindowSize)
    part.Size = Vector2(100,50)
    part.Parent = workspace

PrintTree()
# Root
# └─• Workspace
#     └─• Part 
#     └─• Part 
#     └─• Part 
#     └─• Part 
#     └─• Part 
#     └─• Part 

# Run the game, right now it's in form of a library
Run() 
```



## Coming soon:
- [ ] Add more classes
    - [ ] Finish Part
    - [ ] Sound
    - [ ] Model
    - [ ] Camera
- [ ] Make it threaded the same way Roblox works
- [ ] Serialize Instances into a scene to be loaded
- [ ] Scene editor
