from custom_types import RealGEZ
from coinvolto import Coinvolto
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from impiegato import Impiegato
    

class Progetto:
    _nome: str #noto alla nascita
    _budget: RealGEZ #noto alla nascita
    _impiegato: dict['Impiegato', 'Coinvolto'] #certamente non noto alla nascita


    def __init__(self, nome: str, budget: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegato = {}

    def nome(self) -> str:
        return self._nome

    def budget(self) -> RealGEZ:
        return self._budget

    def impiegato(self) -> dict['Impiegato', 'Coinvolto']:
        return self._impiegato

    def set_nome(self, n: str) -> None:
        self._nome = n

    def set_budget(self, b: RealGEZ) -> None:
        self._budget = b

    def add_impiegato(self, impiegato: 'Impiegato') -> None:
        if impiegato in self._impiegato:
            raise ValueError
        c = Coinvolto(impiegato, self)
        self._impiegato[impiegato] = c

    def remove_impiegato(self, impiegato: 'Impiegato') -> None:
        if impiegato not in impiegato:
            raise ValueError
        self._impiegato.pop(impiegato)
