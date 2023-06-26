Rekommender at du leser denne her: https://docs.google.com/document/d/14ORG8kxilITxYplmJD_6uKYcscgWtNICAaEV6ECTAqg/edit?usp=sharing

Dokumentasjon for Simulering av Spredning av Zombie Virus
Denne koden er en simulering av spredningen av et zombievirus i en befolkning. Den bruker SEIR (Susceptible-Exposed-Infected-Recovered) modellen for å simulere dynamikken i virusets spredning. Simuleringen visualiseres ved hjelp av matplotlib-biblioteket i Python.

Nødvendige Libraries
Koden er avhengig av følgende Python-biblioteker:

matplotlib.pyplot: Brukes til å opprette plottet og visualisere simuleringen.
matplotlib.animation: Brukes til å animere plottet.
numpy: Brukes til numeriske beregninger og array-manipulering.
random: Brukes til å generere tilfeldige tall.
Sørg for at disse bibliotekene er installert i Python-miljøet der koden blir kjørt.

Simulering Parametere
Simuleringen har flere parametere som kan justeres for å kontrollere oppførselen til virusets spredning og andre aspekter av simuleringen. Parametrene og deres initielle verdier er som følger:

men: Initialt antall menn i befolkningen.
women: Initialt antall kvinner i befolkningen.
zombies: Initialt antall zombier i befolkningen.
deaths: Initialt antall dødsfall i befolkningen.
resources: Initialt antall tilgjengelige ressurser.
exposed: Initialt antall personer som er eksponert for viruset.
recovered: Initialt antall personer som har kommet seg etter viruset.
infection_rate: Rate for hvordan viruset sprer seg fra smittede personer til mottakelige personer.
exposure_duration: Varighet av eksponeringsperioden for viruset.
recovery_duration: Varighet av utvinningsperioden fra viruset.
science_group_size: Størrelse på en vitenskapsgruppe som jobber med å finne et motmiddel mot viruset.
antidote_chance: Sjanse for at vitenskapsgruppen utvikler et motmiddel.
wipeout_chance: Sjanse for at vitenskapsgruppen blir utryddet.
Disse parameterne kan justeres for å utforske ulike scenarier og observere effektene på virusets spredning.


Initialisering av Plottet
Koden initialiserer et plott ved hjelp av matplotlib.pyplot. Den oppretter en figur og legger til en enkelt subplot i den. X-aksen representerer tid, og Y-aksen representerer befolkning/ressurser. Plottet vil vise flere linjer som representerer ulike befolkningsgrupper og ressursnivåer over tid.

De initielle grensene for x-aksen og y-aksen er satt basert på de initielle befolkningsverdiene.

Initialisering av Befolkningsdata
Koden initialiserer lister for å lagre befolknings- og ressursdata over tid. Disse listene brukes til å oppdatere plottet under animasjonen. De initielle verdiene for befolkningsdataene blir lagt til i de respektive listene.

Plottlinjer
Koden oppretter flere plottlinjer som vil vise befolknings- og ressursdataene på plottet. Hver linje er knyttet til en spesifikk liste med data.

Oppdatering av Befolkningen
update_population()-funksjonen blir kalt i hver animasjonsrunde for å oppdatere befolkningen basert på spesifikke regler og modeller. Funksjonen inneholder følgende logikk:

Oppdatering av SEIR-modellen: Beregner antall nye eksponerte og antall nye friskmeldte basert på infeksjonsraten og utvinningsvarigheten. Oppdaterer også de eksponerte og friskmeldte populasjonene, samt trekker fra antall nye eksponerte fra menn og kvinner populasjonene.

Zombieinfeksjon og død: Beregner infeksjonsraten for zombier og sjekker om hver person blir infisert. Hvis en person blir infisert, økes dødsfallene, og antall menn eller kvinner reduseres.

Repopulasjon og naturlige dødsfall: Beregner sannsynligheten for repopulasjon basert på antall menn, kvinner, zombier og dødsfall. Hvis sjansen for repopulasjon slår til, legges det til nyfødte babyer i menn og kvinner populasjonene. Beregner også sannsynligheten for naturlige dødsfall og øker dødsfallene med et tilfeldig antall.

Nedbrytning av zombier: Trekker fra et tilfeldig antall zombier for å simulere nedbrytning.

Ressurshåndtering: Trekker fra et tilfeldig antall ressurser for å simulere forbruket.

Sult: Hvis ressursene faller under null, sjekkes det om sult oppstår for hver individ. Hvis sult oppstår, reduseres antall menn og kvinner.

Handlinger fra vitenskapsgruppen: Hvis vitenskapsgruppen er til stede, sjekkes det om de utvikler et motmiddel eller blir utryddet basert på gitte sjanser.

Justering av repopulasjon basert på antall menn og kvinner: Beregner sannsynligheten for repopulasjon igjen og legger til nyfødte babyer hvis sjansen slår til.

Animasjon Funksjon
animate()-funksjonen er en animasjonskalbaksfunksjon som oppdaterer plottet i hver runde. Den kaller update_population()-funksjonen for å oppdatere befolkningen og ressursverdiene. Deretter legger den til de oppdaterte verdiene i de respektive listene for plotting. Til slutt oppdaterer den plottlinjene med de nye dataene.

Funksjonen justerer også grensene for x-aksen og y-aksen dynamisk basert på de nåværende dataene.

Animasjonen stopper hvis enten alle mennesker eller zombier dør ut.

Start av Animasjon
Koden oppretter en animasjonsobjekt ved hjelp av animation.FuncAnimation() og angir animate()-funksjonen som kalles i hver runde. Intervallet mellom hver runde er satt til 100 millisekunder. Animasjonen vises ved hjelp av plt.show().

Konklusjon
Denne koden implementerer en simulering av spredningen av et zombievirus ved hjelp av SEIR-modellen. Den viser befolkningsendringene over tid og gir en visuell representasjon av virusets spredning. Ved å justere parametrene kan du utforske ulike scenarier og observere konsekvensene av endringer i spredningsraten, utvinningsvarigheten og andre faktorer.
