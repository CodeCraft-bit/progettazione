class Nazione:
    _nome: str #noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome (nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, no: str) -> None:
        self._nome: str = no