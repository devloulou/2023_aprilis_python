"""
Adatintegráció
Data pipeline-okat fejleszteni

ETL - ELT

ETL - Extract Transform Load
ELT - Extract Load Transform

Extract: való adat kinyerése valamilyen forrásból - file, adatbázis, API stb.
Transform: a kinyert adat átalakítása:
        - adattisztítás -> pl. mi történjen a hiányzó adatokkal
                        -> egységes formátumra hozni pl. a dátumokat
                        -> ismert / nem ismert adathibák esetén mi történjen
        - adatmodellbe integráljuk az adatot
Load: a transformált adat betöltése a végleges helyre pl. adatbázis

ETL során backend oldalon történik az adat transformációja
ELT során adatbázis oldalon történik az adat transformációja

"""