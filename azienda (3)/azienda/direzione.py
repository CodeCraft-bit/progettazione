from __future__ import annotations
from impiegato import Impiegato
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dipartimento import Dipartimento

class Direzione:
    _impiegato: Impiegato #noto alla nascita
    _dipartimento: list[Dipartimento] #noto alla nascita

    def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento) -> None:
        self._impiegato = impiegato
        self._dipartimento = []
        self._dipartimento.append(dipartimento)

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def dipartimento(self) ->list[Dipartimento]:
        return self._dipartimento
        
    def __repr__(self)->str:
        return f"L' impiegato {self.impiegato()} dirige i seguenti dipartimenti {self.dipartimento()}"