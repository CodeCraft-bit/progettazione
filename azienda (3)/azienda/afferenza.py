from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from impiegato import Impiegato
    from dipartimento import Dipartimento

class Afferenza:
    _impiegato: list[Impiegato] #noto alla nascita
    _dipartimento: Dipartimento #noto alla nascita
    _data_afferenza: datetime #<<immutable>>

    
    def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento, data_afferenza: datetime) -> None:
        self._impiegato = []
        self._impiegato.append(impiegato)
        self._dipartimento = dipartimento
        self._data_afferenza = data_afferenza

    def impiegato(self) -> list[Impiegato]:
        return self._impiegato
    
    def dipartimento(self) ->Dipartimento:
        return self._dipartimento
        
    def data_afferenza(self) -> datetime:
        return self._data_afferenza