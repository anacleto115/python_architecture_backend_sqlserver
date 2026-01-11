from abc import ABC, abstractmethod;

class IEntities:
    @abstractmethod
    def Get_Id(self) -> int:
        pass;
    @abstractmethod
    def GetClone(self) -> object:
        pass;