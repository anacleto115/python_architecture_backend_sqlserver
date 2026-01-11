import sys;
from lib_domain_context import IParser;
from lib_data_core.Core import IConnection;
from lib_data_context.Core import ConnectionSQL;

class Repository:
    parser: IParser.IParser = None;
    connection: IConnection.IConnection = None;

    def Load(self, data: dict) -> None:
        try:
            if data == None or not "Connection" in data.keys(): 
                self.connection = ConnectionSQL.ConnectionSQL(data["stringConnection"]);
            else:
                self.connection = data["Connection"];

            if "KeepConnection" in data.keys(): 
                data["Connection"] = self.connection;
        except:
            raise Exception(sys.exc_info());

    def Execute(self, data: dict, *params) -> dict:
        response: dict = { };
        try:
            self.Load(data);
            if not "Open" in data.keys() or bool(data["Open"]): 
                self.connection.Open();

            cursor = self.connection.Execute(data["Procedure"], *params, "Services", "127.0.0.1");
            
            list_data: list = [];
            for row in cursor:
                list_data.append(self.parser.CreateEntity(row));
                
            if not "Close" in data.keys() or bool(data["Close"]): 
                self.connection.Close();

            response["Entities"] = list_data;
            response["Response"] = "OK";
            return response;
        except:
            response["Error"] = str(sys.exc_info());
            return response;

    def ExecuteNonQuery(self, data: dict, *params) -> dict:
        response: dict = { };
        try:
            self.Load(data);
            if not "Open" in data.keys() or bool(data["Open"]): 
                self.connection.Open();

            result = self.connection.ExecuteNonQuery(data["Procedure"], *params, "Services", "127.0.0.1");
            
            if not "Close" in data.keys() or bool(data["Close"]): 
                self.connection.Close();

            response["Result"] = result;
            response["Response"] = "OK";
            return response;
        except:
            response["Error"] = str(sys.exc_info());
            return response;