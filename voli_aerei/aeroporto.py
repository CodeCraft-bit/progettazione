from città import Città

class Aereoporto:
    _codice: str #noto alla nascita
    _nome: str #noto alla nascita
    _città: Città #noto alla nascita


    def __init__(self, nome: str, codice: str, città: Città) -> None:
        self.set_nome(nome)
        self.set_codice(codice)
        self.set_città(città)
        

    def nome(self) -> str:
        return self._nome

    def codice(self) -> str:
        return self._codice
    
    def città(self) -> Città:
        return self._città

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_codice(self, cd: str) -> None:
        self._codice: str = cd

    def set_città(self, ct: Città) -> None:
        self._città: Città = ct
        