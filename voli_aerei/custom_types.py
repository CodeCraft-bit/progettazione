from typing import Self, Type
import re
from typing import Any





class CAP(str):

    def __new__(cls, v: str | Self) -> Self:
        if re.fullmatch(r"^\d{5}$", v):
            return super().__new__(cls, v)
        raise ValueError(f"'{v}' non è un CAP italiano valido!")
class CAP(str):
    def __new__(cls, v: str | Self) -> Self:
        if re.fullmatch(r"^\d{5}$", v):
            return super().__new__(cls, v)
        raise ValueError(f"'{v}' non è un CAP italiano valido!")

class Indirizzo:
   
    _via:str
    _civico: str
    _cap: CAP
    def __init__(self, via: str, civico: str, cap: CAP) -> None:
        self._via: str = via

        if not re.search("^[0-9]+[a-zA-Z]*$", civico):
            raise ValueError(f"value for civico '{civico}' not allowed")
        self._civico: str = civico
        self._cap: CAP = cap

    def via(self) -> str:
        return self._via

    def civico(self) -> str:
        return self._civico

    def cap(self) -> str:
        return self._cap

    def __repr__(self) -> str:
        return f"Indirizzo(via={self.via()}, civico={self.civico()}, cap={self.cap()})"

    def __str__(self) -> str:
        return f"{self.via()} {self.civico()} - {self.cap()}"

    
    def __hash__(self) -> int:
        return hash((self.via(), self.civico(), self.cap()))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())

class Int:

	def __init__(self, v:int|Self):
		if not isinstance(v, (int, Int) ):
			raise ValueError(f"Value v must be an int or an Int, now {v}")
		self._value = v.value() if isinstance(v, Int) else v

	def value(self)->int:
		return self._value

	def __hash__(self)->int:
		return hash(self.value())
	
	def __eq__(self, other:Any)->bool:
		if other is None:
		
			return False

		if not isinstance(other, Int):
			
			try:
				other = Self(other)
			except:
				
				return False
		
		if hash(self) != hash(other):
			
			return False
		else:
			
			return self.value() == other.value()

class PositiveInt(int):
      
      def __new__(cls,d: int|float|str|bool|Self) -> Self:
            n: int = super().__new__(cls, d)

            if n > 0:
                return n
            raise ValueError(f"Il numero inserito {d} non è positivo!")
      
class IntGEZ(int):
      
	def __new__(cls, v:int|float|Self)->Self:
		if v < 0:
			raise ValueError(f"Value v == {v} must be >= 0")
		return int.__new__(cls, v)    

class Int(int):
      
	def __new__(cls, v:int|float|Self)->Self:
		if v < 1900:
			raise ValueError(f"Value v == {v} must be > 1900")
		return int.__new__(cls, v)      