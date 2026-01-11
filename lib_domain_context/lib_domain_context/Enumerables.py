from enum import Enum;

class Types(Enum):
    Persons = 1
    PersonTypes = 2;

class Architecture(Enum):
    StandAlone = 1
    Services = 2;

class Loading(Enum):
    ADD = 1
    REMOVE = 2;

class Action(Enum):
    OPEN = 1
    CLOSE = 2;