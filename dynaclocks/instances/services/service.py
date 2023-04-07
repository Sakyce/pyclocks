from abc import ABC
from typing import Self, Type, TypeVar


from ..instance import Instance

T = TypeVar('T')

services = []

class Service(Instance):
    def __init__(self) -> None:
        super().__init__()
        
        if type(self) in [type(service) for service in services]:
            raise Exception(f"{self.__class__.__name__} can only be instanciated once.")
        
        services.append(self)

from .root import Root

def GetService(service_to_get:Type[T]) -> T: # first time i used generics on python, that's epic
    # if isinstance(service_to_get, object):
    #     raise Exception()
    
    service_types = [type(service) for service in services]
    for service in services:
        if type(service) == service_to_get:
            return service
        
    service = service_to_get()
    if type(service) != Root:
        service.Parent = GetService(Root) # type: ignore
    return service