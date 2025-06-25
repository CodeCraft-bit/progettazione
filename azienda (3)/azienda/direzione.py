from dipartimento import Dipartimento
from impiegato import Impiegato

class Direzione:
    _impiegato: Impiegato #noto alla nascita
    _dipartimento: Dipartimento #noto alla nascita

    def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento) -> None:
        self._impiegato = impiegato
        self._dipartimento = dipartimento

    def impiegato(self) -> Impiegato:
        return self._dipartimento
    
    def dipartimento(self) -> Dipartimento:
        return self._dipartimento
        