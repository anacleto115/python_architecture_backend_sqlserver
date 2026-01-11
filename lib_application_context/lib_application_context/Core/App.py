import sys;
from lib_data_core.Core import FactoryRepository;
from lib_domain_context import IApplication, IRepository, IParser;
from lib_data_context.Core import FactoryRepositoryContext;

class App(IApplication.IApplication):
    parser: IParser.IParser = None;
    iRepository: IRepository.IRepository = None;

    def Load(self, data: dict) -> dict:
        if FactoryRepository.FactoryRepository.GetFactory() == None:
            FactoryRepository.FactoryRepository.SetFactory(FactoryRepositoryContext.FactoryRepositoryContext());
        if "IRepository" in data.keys(): 
            self.iRepository = data["IRepository"];
        return data;
    
    def Select(self, data: dict) -> dict:
        response: dict = {};
        try:
            data = self.Load(data);
            response = self.iRepository.Select(data);
            if self.parser != None and "Entities" in response.keys():
                list_data: list = response["Entities"];
                count: int = 0;
                dic: dict = { };
                for item in list_data:
                    dic[str(count)] = self.parser.ToDictionary(item);
                    count = count + 1;
                response["Entities"] = dic;
            return response;
        except:
            response["Error"] = str(sys.exc_info());
            return response;

    def Insert(self, data: dict) -> dict:
        response: dict = {};
        try:
            data = self.Load(data);
            if not "Entity" in data.keys():
                response["Error"] = "lbMissingInfo";
                return response;
            if self.parser != None:
                data["Entity"] = self.parser.ToEntity(data["Entity"]);
            if self.parser != None and not self.parser.Validate(data["Entity"]):
                data["Entity"] = self.parser.ToEntity(data["Entity"]);
            response = self.iRepository.Insert(data);
            if self.parser != None and "Entity" in response.keys():
                response["Entity"] = self.parser.ToDictionary(response["Entity"]);
            return response;
        except:
            response["Error"] = str(sys.exc_info());
            return response;

    def Update(self, data: dict) -> dict:
        response: dict = {};
        try:
            data = self.Load(data);
            if not "Entity" in data.keys():
                response["Error"] = "lbMissingInfo";
                return response;
            if self.parser != None:
                data["Entity"] = self.parser.ToEntity(data["Entity"]);
            if self.parser != None and not self.parser.Validate(data["Entity"]):
                data["Entity"] = self.parser.ToEntity(data["Entity"]);
            response = self.iRepository.Update(data);
            if self.parser != None and "Entity" in response.keys():
                response["Entity"] = self.parser.ToDictionary(response["Entity"]);
            return response;
        except:
            response["Error"] = str(sys.exc_info());
            return response;

    def Delete(self, data: dict) -> dict:
        response: dict = {};
        try:
            data = self.Load(data);
            if not "Entity" in data.keys():
                response["Error"] = "lbMissingInfo";
                return response;
            if self.parser != None:
                data["Entity"] = self.parser.ToEntity(data["Entity"]);
            if self.parser != None and not self.parser.Validate(data["Entity"]):
                data["Entity"] = self.parser.ToEntity(data["Entity"]);
            response = self.iRepository.Delete(data);
            if self.parser != None and "Entity" in response.keys():
                response["Entity"] = self.parser.ToDictionary(response["Entity"]);
            return response;
        except:
            response["Error"] = str(sys.exc_info());
            return response;
