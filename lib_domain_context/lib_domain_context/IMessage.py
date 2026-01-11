from enum import Enum;
from abc import ABC, abstractmethod;

class Message(Enum):
    MESSAGE = 1
    QUESTION = 2;

class IMessage:
    @abstractmethod
    def Show(self, message: object, _type: Message = Message.MESSAGE) -> object:
        pass;

class MessagesHelper:
    iMessage: IMessage = None;
    
    @staticmethod
    def Show(message: object, _type: Message = Message.MESSAGE) -> object:
        pass;
        if MessagesHelper.iMessage == None:
            return False;
        return MessagesHelper.iMessage.Show(message, _type);