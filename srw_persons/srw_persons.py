import sys;
import datetime;
from flask import Flask, jsonify, request;
from srw_persons.Implementations import TokenService;
from srw_persons.Implementations import PersonTypesService;
app = Flask(__name__);

personTypesService = PersonTypesService.PersonTypesService();
tokenService = TokenService.TokenService();

@app.route('/Token/Authenticate', methods=["Post"])
def Token_Authenticate() -> str :
    return tokenService.Authenticate();

@app.route('/PersonTypes/Select', methods=["Post"])
def PersonTypes_Select() -> str :
    return personTypesService.Select(request.data);

if __name__ == "__main__":
    app.run('localhost', 4040);