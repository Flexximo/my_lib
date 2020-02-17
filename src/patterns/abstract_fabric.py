from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def createTigers(self) -> AbstractTiger:
        pass
    def createHorses(self) -> AbstractHorse:
        pass

class WhiteHorseTigerFactory(AbstractFactory):
    def createTigers(self) -> WhiteTiger:
        return WhiteTiger()
    def createHorses(self) -> WhiteHorse:
        return WhiteHorse()


class BlackHorseBlueTigerFactory(AbstractFactory):
    def createTigers(self) -> BlueTiger:
        return BlueTiger()
    def createHorses(self) -> BlackHorse:
        return BlackHorse()


###

class AbstractHorse(ABC):
    def function_h(self) -> str:
        pass

class WhiteHorse(AbstractHorse):
    def function_h(self) -> str:
        return "I am white horse"

class BlackHorse(AbstractHorse):
    def function_h(self) -> str:
        return "I am black horse"
###

###
class AbstractTiger(ABC):
    def function_t(self) -> None:
        pass
    def bites(self, victim: AbstractHorse) -> None:
        pass

class WhiteTiger(AbstractTiger):
    def function_t(self) -> str:
        return "I am a white tiger"
    def bites(self, victim: AbstractHorse) -> str:
        result = victim.function_h()
        return f"white tiger eaten horse who says {result}"    

class BlueTiger(AbstractTiger):
    def function_t(self) -> str:
        return "I am a blue tiger"
    def bites(self, victim: AbstractHorse) -> str:
        result = victim.function_h()
        return f"Blue tiger eaten horse who says {result}" 
###

def client_code(factory: AbstractFactory) -> None:
    product_a = factory.createTigers()
    product_b = factory.createHorses()
    
    print