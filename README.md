# Clocks : A PyGame Framework inspired by Roblox
### Still a work in progress


## Very simple to use
```py
from dynaclocks import *

# Get the Workspace to put our parts in
workspace = GetService(Workspace)

# Create 6 Parts with a randomized position
for i in range(6):
    part = Part()
    part.Position = Vector2.RandomBetween(0,0,*Settings.WindowSize)
    part.Size = Vector2(100,50)
    part.Parent = workspace

# Print the entire tree
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
    - [ ] Model & Folder
    - [ ] Sprite (& probably Humanoid)
    - [ ] Camera
- [ ] Make it threaded the same way Roblox works and hope for a fair async await syntax
- [ ] Make scripts executed as modules
- [ ] Serialize Instances into a scene to be loaded
- [ ] Scene editor

## Contributing
At little help doesn't hurt ig, create an issue for any request or bug you find.
You can also contact me on Discord: `Mélody#2638`