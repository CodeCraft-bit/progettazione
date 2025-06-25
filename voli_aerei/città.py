from custom_types import IntGEZ
from aeroporto import Aereoporto

class Città:
    _nome: str #noto alla nascita
    _abitanti: IntGEZ #noto alla nascita

    def __init__(self,*, nome: str, abitanti: IntGEZ) -> None:
        self.set_nome (nome)
        self.set_abitanti = abitanti

    def nome(self) -> str:
        return self._nome
    
    def abitanti(self) -> IntGEZ:
        return self._abitanti
    
    def set_nome(self, nm: str) -> None:
        self._nome: str = nm

    def set_abitanti(self, a: IntGEZ) -> None:
        self._abitanti: IntGEZ = a
        


