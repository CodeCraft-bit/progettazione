from __future__ import annotations
from custom_types import Telefono, Indirizzo
from direzione import Direzione
from typing import TYPE_CHECKING
from datetime import datetime
from afferenza import Afferenza

if TYPE_CHECKING:
    from impiegato import Impiegato
    

class Dipartimento:

    _nome: str # noto alla nascita
    _telefoni: set[Telefono] # [1..*] noto alla nascita
    _indirizzo: Indirizzo | None  # [0..1] possibilmente non noto alla nascita
    _direzione: dict[Direzione]
    _afferenza: dict[Afferenza]


    def __init__(self, nome: str, tel: Telefono, ind: Indirizzo|None) -> None:
        self.set_nome(nome)

        # opzione 1
        self._telefoni = set()
        self.add_telefono(tel)
        # opzione 2
        # self.set_telefoni({tel})

        self.set_indirizzo(ind)
        self._direzione = {}
        self._afferenza = {}

    def nome(self) -> str:
        return self._nome

    def indirizzo(self) -> Indirizzo | None:
        return self._indirizzo

    def telefoni(self) -> frozenset[Telefono]:
        return frozenset(self._telefoni)

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_indirizzo(self, i: Indirizzo | None) -> None:
        self._indirizzo = i

    def add_telefono(self, telefono: Telefono) -> None:
        self._telefoni.add(telefono)

    def set_telefoni(self, telefoni: set[Telefono]) -> None:
        if not telefoni: # equivalente a len(telefoni) == 0
            raise ValueError("Il dipartimento deve avere almeno un numero di telefono")
        self._telefoni = telefoni

    def remove_telefono(self, telefono: Telefono) -> None:
        if len(self._telefoni) >= 2: # telefono è [1..*]!
            self._telefoni.remove(telefono)
        else:
            raise RuntimeError("Il dipartimento deve avere almeno un numero di telefono")

    def __str__(self):
        if self._indirizzo is None:
            ind_str: str = "senza sede"
        else:
            ind_str: str = f"con sede in {self.indirizzo()}"

        return f"Dipartimento '{self.nome()}' {ind_str} e numeri telefono: {self.telefoni()}"
    
    def direzione(self) -> dict[Impiegato, Direzione]:
       return self._direzione
    
    def add_link_direzione(self, impiegato: Impiegato) -> None:
        
        for x in self._direzione.values():
            if x.impiegato() == impiegato:
                for y in x.dipartimento():
                    if y == self:
                        raise ValueError('Il dipartimento è già presente')
                    else:
                        x.dipartimento().append(self)
        d = Direzione(impiegato, self)
        self._direzione['Link'] = d
        return self._direzione
    
    def add_link_afferenza(self, impiegato: Impiegato, data_afferenza: datetime = datetime.now()) -> None:
        for x in self._afferenza.values():
            if x.dipartimento() == self:
                for y in x.impiegato():
                    if y == impiegato:
                        raise ValueError("L'impiegato è già presente")
                    else:
                        y.impiegato().append(impiegato)
        a = Afferenza(impiegato, self, data_afferenza)
        self._afferenza['Link'] = a
        return self._afferenza





if __name__ == "__main__":
    pass