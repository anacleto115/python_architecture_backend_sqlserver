from lib_domain_context import IConfiguration;

class Configuration(IConfiguration.IConfiguration):
    def Get(self, key: str) -> str:
        return """Driver={SQL Server};
                  Server=localhost;
                  Database=db_persons;
                  PORT=1433;
                  user=sa;
                  password=*****;""";