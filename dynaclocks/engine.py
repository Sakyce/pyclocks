from .instances.services.root import Root
from . import *
from .instances.services import service as Services
from .instances.instance import Instance
from .instances.part import Part

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def Run():
    pygame.init()
    screen = pygame.display.set_mode((Settings.WindowSize.X, Settings.WindowSize.Y))
    clock = pygame.time.Clock()

    workspace = Services.GetService(Workspace)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for inst in workspace.GetChildren():
            if type(inst) == Part:
                rect = pygame.Rect(
                    inst.Position.X,
                    inst.Position.Y,
                    inst.Size.X,
                    inst.Size.Y
                )
                pygame.draw.rect(screen,"red",rect)
                
        pygame.display.flip()
        screen.fill("black")
        clock.tick(60)

def Tree(root:Instance|None=None, markerStr="├─• ", levelMarkers=[]):
    if root is None:
        root = Services.GetService(Root)
    emptyStr = " "*len(markerStr)
    connectionStr = "│" + emptyStr[:-1]
    level = len(levelMarkers)
    mapper = lambda draw: connectionStr if draw else emptyStr
    
    markers = "".join(map(mapper, levelMarkers[:-1]))
    markers += markerStr if level > 0 else ""

    yield f"{markers}{root.Name}"

    for i, child in enumerate(root.GetChildren()):
        isLast = i == len(root.GetChildren()) - 1
        yield from Tree(child, "└─• " if isLast else markerStr, [*levelMarkers, not isLast])

def PrintTree(root:Instance|None=None):
    for node in Tree(root):
        print(node)