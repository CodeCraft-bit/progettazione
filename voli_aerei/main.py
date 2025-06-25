from custom_types import *
from volo import Volo
from aeroporto import Aereoporto
from città import Città
from compagnia import Compagnia

aer: Aereoporto = Aereoporto("Aereoporto di Fiumicino","0012345", "Roma")
print(f"Ho creato l'{aer.nome()} con codice {aer.codice()} situato in {aer.città()}")

vol: Volo = Volo("15578", 12, "Aereoporto di Fiumicino", "Aereoporto di Malpensa", "Ryanair")
print(f"Ho creato il volo con codice {vol.codice()} e durata di ore {vol.durata_min()} con arrivo dall'{vol.aereoporto_arrivo()} e partenza dall'{vol.aereoporto_partenza()} accompagnati dalla compagnia {vol.v_compagnia()}")

