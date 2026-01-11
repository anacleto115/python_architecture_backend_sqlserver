class Parameters:
    name: str = None;
    type: int = None;
    value: object = None;
    direction: bool = False;
    
    def __init__(self, name: str, type: int, value: object, direction: bool):
        self.name = name;
        self.type = type;
        self.value = value;
        self.direction = direction;
        
    def GetName(self) -> str:
        return self.name;
    def SetName(self, value: str) -> None:
        self.name = value;
        
    def GetType(self) -> int:
        return self.type;
    def SetType(self, value: int) -> None:
        self.type = value;
        
    def GetValue(self) -> object:
        return self.value;
    def SetValue(self, value: object) -> None:
        self.value = value;
        
    def GetDirection(self) -> bool:
        return self.direction;
    def SetDirection(self, value: bool) -> None:
        self.direction = value;
