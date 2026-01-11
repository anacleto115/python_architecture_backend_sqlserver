import sys;
import datetime;
from lib_service_core.Core import IToken;
from lib_domain_context import ServiceData;
from lib_utilities.Utilities import JsonHelper;

class TokenService(IToken.IToken):
    def Authenticate(self) -> str :
        response: dict = { };
        try:
            response["Token"] = ServiceData.ServiceData.KeyToken();
            response["Expires"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Send"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Validate(self, data: dict) -> bool:
        try:
            if data == None or not "Bearer" in data.keys():
                return False;
            bearer: str = data["Bearer"];
            if ServiceData.ServiceData.KeyToken() != bearer:
                return False;
            return True;
        except:
            return False;