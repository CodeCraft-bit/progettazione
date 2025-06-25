from custom_types import Int

class Compagnia:
    _nome: str #noto alla nascita
    _anno: Int #<<immutable>>, noto alla nascita

    def __init__(self, nome: str, anno: Int) -> None:
        self._nome(nome)
        self._anno = anno

    
    def nome(self) -> str:
        return self._nome
    
    def anno(self) -> Int:
        return self._anno
    
    def set_nome(self, no: str) -> None:
        self._nome: str = no

    def set_anno(self, an: Int) -> None:
        self._anno: Int = an
        