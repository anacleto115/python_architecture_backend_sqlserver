from lib_domain_context import IParser;
from lib_domain_entities.Models import PersonTypes;

class PersonTypesParser(IParser.IParser):
    def CreateEntity(self, ItemArray: list) -> object:
        entity = PersonTypes.PersonTypes();
        entity.SetId(ItemArray[0]);
        entity.SetName(ItemArray[1]);
        return entity;

    def ToEntity(self, data: dict) -> object:
        entity = PersonTypes.PersonTypes();
        entity.SetId(data["Id"]);
        if "Name" in data.keys(): 
            entity.SetName(data["Name"]);
        return entity;

    def ToDictionary(self, obj: object) -> dict:
        entity: PersonTypes.PersonTypes = obj;

        response: dict = { };
        response["Id"] = entity.GetId();
        if entity.GetName() != None and entity.GetName() != "": 
            response["Name"] = entity.GetName();
        return response;

    def Validate(self, obj: object) -> bool:
        entity: PersonTypes.PersonTypes = obj;

        if entity.GetName() == None or entity.GetName() == "": 
            return False;
        return True;