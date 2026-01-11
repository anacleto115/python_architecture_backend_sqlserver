import copy

from lib_domain_context import IEntities;

class PersonTypes(IEntities.IEntities):
    id: int = 0;

    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    name: str = None;

    def GetName(self) -> int:
        return self.name;
    def SetName(self, value: int) -> None:
        self.name = value;

    def Get_Id(self) -> int:
        return self.id;
    def GetClone(self) -> object:
        return copy.copy(super()); 
