#Opis delavnice

Ena izmed pomembnejših lastnosti programskega jezika Python so dinamični in še pomembneje "račji" tipi. Vendar pa tako odprt pristop lahko pokaže težave pri večjih projektih, saj s tem izgubimo možnost predčasnega odkrivanja napak. Na delavnici si bomo pogledali orodje mypy, ki nam omogoča opcijsko dodajanje in preverjanje tipov na že obstoječ python program, a se hkrati ne vmešava v samo izvajanje programa. Če bo ostal čas, pa si bomo pogledali še nekaj skrivnosti, ki jih python skriva pri delu z razredi, poskušali narediti naše objekte še nekoliko bolj dinamične, ali pa jih popolnoma zakleniti in s tem prihraniti kar nekaj časa in prostora.

Delavnica bo razdeljena na 3 dele.

## Spoznavanje orodja mypy in anotacij
Najprej si bomo na obstoječi python skripti pogledali, kako sploh izgleda dodajanje tipov na program, kako uporabljamo mypy in kako razumemo napake, ki nam jih javi. Nekoliko bomo pokukali tudi v konfiguracijsko datoteko in izklopili stvari, ki nam bodo šle na živce. Pogledali bomo tudi kako mypy deluje z novo definiranimi tipi in kako se obnaša v generatorjih, razredih, pri dedovanju...


## Odkrivanje napak
Na že spisan program sestavljen iz več razredov bomo dodali tipe in poskušali najti napako.

## Kaj skrivajo objekti
Da lahko objekte uporabljamo še bolj nam jezik omogoča kar nekaj bljižnjic, ki pa so občano skrite. Če bo ostal čas si bomo pogledali, kako lahko uporabljamo "lastnosti" (properties) namesto "geterjev", kako na razredu dinamično definiramo nove metode in atribute, ter kako lahko s pomočjo atributa `__slots__` preprečimo nepotrebno porabo spomina in s tem povečamo hitrost programa (in kakšne težave to prinese).

## Priporočeno predznanje:
Osnovno znanje Pythona in git-a, v pomoč bo znanje vsaj enega statično tipiziranega jezika (npr. C, C++, Java, C#). 
