from abc import ABC, abstractmethod;

class IConnection:
    @abstractmethod
    def Execute(self, query: str, *params) -> object:
        pass;
    
    @abstractmethod
    def ExecuteNonQuery(self, query: str, *params) -> int:
        pass;

    @abstractmethod
    def Open(self) -> None:
        pass;

    @abstractmethod
    def Close(self) -> None:
        pass;