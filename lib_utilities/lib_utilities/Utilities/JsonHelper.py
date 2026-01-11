import json;

class JsonHelper:
    @staticmethod
    def ConvertToString(data: dict) -> str:
        response: str = json.dumps(data)
        return response;

    @staticmethod
    def ConvertToObject(data: str, repeat: int = 0) -> dict:
        response: dict = json.loads(data);
        for count in range(0, repeat, 1):
            response = json.loads(response);
        return response;

