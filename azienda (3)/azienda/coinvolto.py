from impiegato import Impiegato
from progetto import Progetto

class Coinvolto:
    _impiegato: Impiegato #noto alla nascita <<immutable>>
    _progetto: Progetto #noto alla nascita <<immutable>>

    def __init__(self, impiegato: Impiegato, progetto: Progetto) -> None:
        self._impiegato = impiegato
        self._progetto = progetto

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def progetto(self) -> Progetto:
        return self._progetto
        