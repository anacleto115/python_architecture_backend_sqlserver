import pyodbc;
from lib_data_core.Core import IConnection;

class ConnectionSQL(IConnection.IConnection):
    connection = None;
    stringConnection: str = None;
    
    def __init__(self, stringConnection: str):
        self.stringConnection = stringConnection;
        
    def Execute(self, query: str, *params) -> object:
        cursor = self.connection.cursor();
        return cursor.execute(query, params);
    
    def ExecuteNonQuery(self, query: str, *params) -> int:
        cursor = self.connection.cursor();
        cursor.execute(query, params);
        return int(cursor.fetchone()[0]);

    def Open(self) -> None:
        self.connection = pyodbc.connect(self.stringConnection);

    def Close(self) -> None:
        if self.connection == None:
            return;
        self.connection.close();
        self.connection = None;