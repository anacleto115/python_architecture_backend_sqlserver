import sys;
from flask import jsonify;
from srw_persons import Configuration;
from srw_persons.Implementations import TokenService;
from lib_domain_context import IService, IApplication, IConfiguration, Enumerables;
from lib_service_core.Core import IToken;
from lib_application_context.Core import FactoryApplicationContext;
from lib_application_core.Core import FactoryApplication;
from lib_utilities.Utilities import JsonHelper;

class ServiceBase(IService.IService):
    iApp: IApplication.IApplication = None;
    iToken: IToken = None;
    iConfiguration: IConfiguration.IConfiguration = None;
    
    def Load(self, data: dict) -> dict:
        if self.iConfiguration == None:
            self.iConfiguration = Configuration.Configuration();
        data["stringConnection"] = self.iConfiguration.Get("Default");
        data["Architecture"] = Enumerables.Architecture.Services
        if FactoryApplication.FactoryApplication.GetFactory() == None:
            FactoryApplication.FactoryApplication.SetFactory(FactoryApplicationContext.FactoryApplicationContext());
        if self.iToken == None:
            self.iToken = TokenService.TokenService();
        if "IApplication" in data.keys(): 
            self.IApplication = data["IApplication"];
        return data;

    def Select(self, income: str) -> str :
        response: dict = { };
        try:
            data = JsonHelper.JsonHelper.ConvertToObject(income);
            data = self.Load(data);
            if not self.iToken.Validate(data):
                response["Error"] = "NoAuthenticate";
                return response;
            if data == None:
                response["Error"] = "lbMissingInfo";
                return response;
            if "Error" in data.keys():
                return jsonify(response);
            response = self.iApp.Select(data);
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Insert(self, income: str) -> str :
        response: dict = { };
        try:
            data = JsonHelper.JsonHelper.ConvertToObject(income);
            data = self.Load(data);
            if not self.iToken.Validate(data):
                response["Error"] = "NoAuthenticate";
                return response;
            if data == None:
                response["Error"] = "lbMissingInfo";
                return response;
            if "Error" in data.keys():
                return jsonify(response);
            response = self.iApp.Insert(data);
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Update(self, income: str) -> str :
        response: dict = { };
        try:
            data = JsonHelper.JsonHelper.ConvertToObject(income);
            data = self.Load(data);
            if not self.iToken.Validate(data):
                response["Error"] = "NoAuthenticate";
                return response;
            if data == None:
                response["Error"] = "lbMissingInfo";
                return response;
            if "Error" in data.keys():
                return jsonify(response);
            response = self.iApp.Update(data);
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Delete(self, income: str) -> str :
        response: dict = { };
        try:
            data = JsonHelper.JsonHelper.ConvertToObject(income);
            data = self.Load(data);
            if not self.iToken.Validate(data):
                response["Error"] = "NoAuthenticate";
                return response;
            if data == None:
                response["Error"] = "lbMissingInfo";
                return response;
            if "Error" in data.keys():
                return jsonify(response);
            response = self.iApp.Delete(data);
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);