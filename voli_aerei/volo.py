from custom_types import PositiveInt
from aeroporto import Aereoporto
from compagnia import Compagnia

class Volo:
    _codice: str #<<immutable>>, noto alla nascita
    _durata_min: PositiveInt #noto alla nascita
    _aereoporto_arrivo: Aereoporto #noto alla nascita
    _aereoporto_partenza: Aereoporto #noto alla nascita
    _v_compagnia: Compagnia #noto alla nascita

    def __init__(self, codice: str, durata_min: PositiveInt, aereoporto_arrivo: Aereoporto, aereoporto_partenza: Aereoporto, v_compagnia: Compagnia) -> None:
        self.set_codice(codice)
        self.set_durata_min(durata_min)
        self.set_aereoporto_arrivo(aereoporto_arrivo)
        self.set_aereoporto_partenza(aereoporto_partenza)
        self.set_v_compagnia(v_compagnia)

    def codice(self) -> str:
        return self._codice
    
    def durata_min(self) -> PositiveInt:
        return self._durata_min
    
    def aereoporto_arrivo(self) -> Aereoporto:
        return self._aereoporto_arrivo
    
    def aereoporto_partenza(self) -> Aereoporto:
        return self._aereoporto_partenza
    
    def v_compagnia(self) -> Compagnia:
        return self._v_compagnia

    def set_codice(self, c: str) -> None:
        self._codice: str = c

    def set_durata_min(self, d: PositiveInt) -> None:
        self._durata_min: PositiveInt = d 

    def set_aereoporto_arrivo(self, a_a: Aereoporto) -> None:
        self._aereoporto_arrivo: Aereoporto = a_a

    def set_aereoporto_partenza(self, a_p: Aereoporto) -> None:
        self._aereoporto_partenza: Aereoporto = a_p

    def set_v_compagnia(self, v_c: Compagnia) -> None:
        self._v_compagnia: Compagnia = v_c
        
