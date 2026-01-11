import sys;
from lib_data_core.Interfaces import IPersonTypesRepository;
from lib_infrastructure.Implementations import PersonTypesParser;
from lib_domain_entities.Models import PersonTypes;
from lib_data_context.Core import Repository;

class PersonTypesRepository(Repository.Repository, IPersonTypesRepository.IPersonTypesRepository):
    def __init__(self, data: dict):
        self.parser = PersonTypesParser.PersonTypesParser();

    def Select(self, data: dict) -> dict:
        response: dict = { };
        try:
            data["Procedure"] = """SET NOCOUNT ON;
                                   DECLARE @result INT
                                   EXEC sp_select_per_types ?,?, @result OUTPUT; 
                                   SELECT @result;""";
            response = self.Execute(data);
            if response == None:
                response["Error"] = "lbNoAnswerDB";
                return response;
            if "Error" in response.keys(): 
                return response;
            response["Response"] = "OK";
            return response;
        except:
            response["Error"] = str(sys.exc_info());
            return response;

    def Insert(self, data: dict) -> dict:
        raise Exception("NotImplemented");

    def Update(self, data: dict) -> dict:
        raise Exception("NotImplemented");

    def Delete(self, data: dict) -> dict:
        raise Exception("NotImplemented");
