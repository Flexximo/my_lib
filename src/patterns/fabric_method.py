# from __future__ import annotations
from abc import ABC, abstractmethod

class GenerateMessageFilterMain(ABC):
    
    @abstractmethod
    def factory_method():
        return "Filtered with default options"

    def some_operation(self): 
        import datetime
        return f"message created on {datetime.datetime.now()}"

class FilterClientMessage(GenerateMessageFilterMain):
    def factory_method(self):
        return ClientMessage()

class FilterServerMessage(GenerateMessageFilterMain):
    def factory_method(self):
        return  ServerMessage()

#interface
class Message(ABC):
    def removable(self) -> str:
        pass
    def storable(self) -> str:
        pass

#classes are implemented with this interface
class ClientMessage(Message):
    def removable(self):
        return "Client message is removable and only"
    def storable(self):
        pass
class ServerMessage(Message):
    def removable(self):
        return "Removable type"
    def storable(self):
        return "Storable"
    
def client(messagefilter: GenerateMessageFilterMain) -> None:
    print("I am on client side, working via base interface!\n"
          f"{messagefilter.some_operation()}")

if __name__ == "__main__":
    print("Message client filter")
    client(FilterClientMessage())
    print("\n")

    print("Mesage server filter")
    client(FilterServerMessage())