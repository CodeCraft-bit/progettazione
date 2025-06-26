from __future__ import annotations
from custom_types import *
from datetime import datetime


class Persona:
    _nome: str
    _cognome: str
    _cf: list[CodiceFiscale] # [1..*]
    _genere: Genere
    _maternita: IntGEZ # [0..1] - deve avere un valore se e solo se _genere = Genere.donna
    _posizione_mil: PosizioneMilitare | None # [0..1] da aggregazione, deve avere un valore se e solo se _genere = Genere.uomo
    _nascita: datetime
    def __init__(self, *, nome: str, cognome: str,
                 cf: list[CodiceFiscale],
                 genere: Genere,
                 maternita: IntGEZ|None=None, nascita: datetime) -> None:
        self._nome = nome
        self._cognome = cognome
        self._nascita = nascita
        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")

        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.diventa_donna(maternita)

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> datetime:
        return self._nascita
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def diventa_donna(self, maternita: IntGEZ) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self.set_maternita(maternita)
        self.__dimentica_uomo()

    def __dimentica_uomo(self) -> None:
        # Questo metodo è privato perché non deve essere mai invocato dall'esterno, ma solo all'interno di questa classe
        self._posizione_mil = None

    def set_maternita(self, maternita: IntGEZ) -> None:
        if not self._genere == Genere.donna:
            raise RuntimeError("Gli uomini non hanno il numero di maternità!")


class Impiegato(Persona):
    _stipendio: RealGEZ
    _ruolo: Ruolo
    _is_responsabile: bool #[0..1]

    def __init__(self, *, nome, cognome, cf, genere, maternita = None, nascita, stipendio: RealGEZ, ruolo: Ruolo) -> None:
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, nascita=nascita)
        self._setstipendio(stipendio)
        self._setruolo(ruolo)
        self._set_is_responsabile()

    def stipendio(self):
        return self._stipendio
    
    def ruolo(self):
        return self._ruolo
    
    def is_responsabile(self):
        return self._is_responsabile
    
    def set_is_responsabile(self):
        if self.ruolo() == Ruolo.progettista:
            self._is_responsabile = True
        else:
            self._is_responsabile = False
    
    def set_ruolo(self, ruolo: Ruolo):
        self._ruolo = ruolo
    
    def set_stipendio(self, stipendio: RealGEZ):
        self._stipendio = stipendio

    def diventa_segretario(self):
        self._ruolo = Ruolo.segretario

    def diventa_direttore(self):
        self._ruolo = Ruolo.direttore

    def diventa_progettista(self):
        self._ruolo = Ruolo.progettista
        self.set_is_responsabile() = True

class Studente(Persona):
    def __init__(self, *, nome, cognome, cf, genere, maternita = None, nascita, matricola: IntGEZ) -> None:
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, nascita=nascita)
        self._matricola = matricola

    def matricola(self):
        return self._matricola


class Progetto:
    _nome: str #noto alla nascita

    def __init__(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    
class PosizioneMilitare:
    _nome: str #<<immutable>>

    def __init__(self, nome: str) -> str:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n


class  resp_prog:
    class _link:
        _impiegato:set[Impiegato] #non noto alla nascita
        _progetto:set[Progetto] #non noto alla nascita

        def init(self, impiegato, progetto):
            self.set_impiegato(impiegato)
            self.set_progetto(progetto)

        def impiegato(self):
            return frozenset[self._impiegato]

        def progetto(self):
            return frozenset[self._progetto]

        def set_impiegato(self, impiegato:set[Impiegato]):
            self._impiegato = impiegato

        def set_progetto(self, progetto:set[Progetto]):
            self._progetto = progetto


        

