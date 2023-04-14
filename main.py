import datetime
import sys

from database_connection_singleton import DatabaseConnectionSingleton
from kontrola_vstupu import *
from reziser import *
from kategorie import *
from kinosal import *
from film import *
from promitani import *
from pohledy import *

if __name__ == '__main__':
    print('Vítejte v programu pro práci s databází v kině')
    DatabaseConnectionSingleton.begin_transaction()
    while True:
        print('MENU')
        print('1...Vypsat všechy filmy')
        print('2...Vypsat všechy kategorie filmů')
        print('3...Vypsat všechy kinosály')
        print('4...Vypsat všecha promítání')
        print('5...Vypsat všechy režiséry')
        print('6...Vypsat přehled filmů')
        print('7...Vypsat přehled promítání')
        print('8...Přidat nový film')
        print('9...Přidat nový kinosál')
        print('10...Přidat nové promítání')
        print('11...Přidat nového režiséra')
        print('12...Upravit film')
        print('13...Upravit kinosál')
        print('14...Upravit promítání')
        print('15...Upravit režiséra')
        print('16...Smazat film')
        print('17...Smazat kinosál')
        print('18...Smazat promítání')
        print('19...Vypsat celkový promítací čas')
        print('20...Ukončit program')
        volba = vstup_cislo(1, 20)
        if volba == 1:
            print('Všechny filmy')
            print(get_all_film())
        elif volba == 2:
            print('Všechny kategorie filmů')
            print(get_all_kategorie())
        elif volba == 3:
            print('Všechny kinosály')
            print(get_all_kinosal())
        elif volba == 4:
            print('Všechna promítání')
            print(get_all_promitani())
        elif volba == 5:
            print('Všichni režiséři')
            print(get_all_reziser())
        elif volba == 6:
            print('Přehled filmů')
            print(get_all_prehled_filmu())
        elif volba == 7:
            print('Přehled promítání')
            print(get_all_prehled_promitani())
        elif volba == 8:
            if not get_reziser_row_count() == 0 and not get_kategorie_row_count() == 0:
                print('Kategorie')
                print(get_all_kategorie())
                print('Režiséři')
                print(get_all_reziser())
                print('Zadej id kategorie z tabulky výše')
                kategorie_id = vstup_cislo(1, get_kategorie_row_count())
                print('Zadej id režiséra z tabulky výše')
                reziser_id = vstup_cislo(1, get_reziser_row_count())
                print('Zadej název nového filmu (2 - 50 znaků)')
                nazev = vstup_text()
                print('Zadej délku filmu v minutách (0 - 480 minut)')
                delka_min = vstup_cislo(0, 480)
                print('Zadej cenu za vstupenku na film v Kč (100 - 1000 Kč)')
                cena = vstup_cislo(100, 1000)
                print('Bude film ve 3D? (1...ano, 2...ne)')
                tri_d = vstup_cislo(1, 2)
                if tri_d == 1:
                    tri_d = True
                else:
                    tri_d = False
                print('Potvrďte přidání filmu (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    add_film(kategorie_id, reziser_id, nazev, delka_min, cena, tri_d)
                    print('Film byl úspěšně přidán')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Přidání filmu bylo zrušeno')
        elif volba == 9:
            print('Zadej označení nového kinosálu (1 - 50 znaků)')
            oznaceni = vstup_text(1, 50)
            print('Zadej kapacitu nového kinosálu (10 - 300)')
            kapacita = vstup_cislo(10, 300)
            print('Potvrďte přidání kinosálu (1...ano, 2...ne)')
            potvrzeni = vstup_cislo(1, 2)
            if potvrzeni == 1:
                add_kinosal(oznaceni, kapacita)
                print('Kinosál byl úspěšně přidán')
                DatabaseConnectionSingleton.commit_transaction()
                DatabaseConnectionSingleton.begin_transaction()
            else:
                print('Přidání kinosálu bylo zrušeno')
        elif volba == 10:
            if not get_film_row_count() == 0 and not get_kinosal_row_count() == 0:
                print('Filmy')
                print(get_all_film())
                print('Kinosály')
                print(get_all_kinosal())
                print('Zadej id filmu z tabulky výše')
                film_id = vstup_cislo(1, get_film_row_count())
                print('Zadej id kinosálu z tabulky výše')
                kinosal_id = vstup_cislo(1, get_kinosal_row_count())
                datum_cas = None
                ok = False
                while not ok:
                    try:
                        print('Zadej den promítání')
                        den = vstup_cislo(1, 31)
                        print('Zadej měsíc promítání')
                        mesic = vstup_cislo(1, 12)
                        print('Zadej rok promítání')
                        rok = vstup_cislo(1900, date.today().year)
                        print('Zadej hodinu promítání')
                        hodina = vstup_cislo(10, 23)
                        print('Zadej minutu promítání')
                        minuta = vstup_cislo(0, 59)
                        datum_cas = datetime(rok, mesic, den, hodina, minuta)
                        print(datum_cas)
                        ok = True
                    except:
                        print('Chyba v datumu, zkuste to znovu')
                print('Potvrďte přidání promítání (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    add_promitani(film_id, kinosal_id, datum_cas)
                    print('Promítání bylo úspěšně přidáno')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Přidání promítání bylo zrušeno')
        elif volba == 11:
            print('Zadej jméno nového režiséra')
            jmeno = vstup_text()
            print('Zadej příjmení nového režiséra')
            prijmeni = vstup_text()
            print('Potvrďte přidání režiséra (1...ano, 2...ne)')
            potvrzeni = vstup_cislo(1, 2)
            if potvrzeni == 1:
                add_reziser(jmeno, prijmeni)
                print('Režisér byl úspěšně přidán')
                DatabaseConnectionSingleton.commit_transaction()
                DatabaseConnectionSingleton.begin_transaction()
            else:
                print('Přidání režiséra bylo zrušeno')

        elif volba == 12:
            if not get_film_row_count() == 0:
                print('Filmy')
                print(get_all_prehled_filmu())
                print('Režiséři')
                print(get_all_reziser())
                print('Kategorie')
                print(get_all_kategorie())
                print('Zadej id filmu z tabulky výše')
                id = vstup_cislo(1, get_film_row_count())
                print('Zadej id kategorie z tabulky výše')
                kategorie_id = vstup_cislo(1, get_kategorie_row_count())
                print('Zadej id režiséra z tabulky výše')
                reziser_id = vstup_cislo(1, get_reziser_row_count())
                print('Zadej název filmu')
                nazev = vstup_text()
                print('Zadej délku filmu v minutách (0 - 480)')
                delka_min = vstup_cislo(0, 480)
                print('Zadej cenu vstupenky na tento film (100 - 1000)')
                cena = vstup_cislo(100, 1000)
                print('Bude film ve 3D? (1...ano, 2...ne)')
                tri_d = vstup_cislo(1, 2)
                if tri_d == 1:
                    tri_d = True
                else:
                    tri_d = False
                print('Potvrďte úpravu filmu (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    change_film(id, kategorie_id, reziser_id, nazev, delka_min, cena, tri_d)
                    print('Film byl úspěšně upraven')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Úprava filmu byla zrušena')
        elif volba == 13:
            if not get_kinosal_row_count() == 0:
                print('Kinosály')
                print(get_all_kinosal())
                print('Zadej id kinosálu z tabulky výše')
                id = vstup_cislo(1, get_kinosal_row_count())
                print('Zadej označení kinosálu (1 - 50 znaků)')
                oznaceni = vstup_text(1, 50)
                print('Zadej kapacitu kinosálu (10 - 300)')
                kapacita = vstup_cislo(10, 300)
                print('Potvrďte úpravu kinosálu (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    change_kinosal(id, oznaceni, kapacita)
                    print('Kinosál byl úspěšně upraven')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Úprava kinosálu byla zrušena')
        elif volba == 14:
            if not get_promitani_row_count() == 0:
                print('Promítání')
                print(get_all_prehled_promitani())
                print('Filmy')
                print(get_all_prehled_filmu())
                print('Kinosály')
                print(get_all_kinosal())
                print('Zadej id promítání')
                id = vstup_cislo(1, get_promitani_row_count())
                print('Zadej id filmu z tabulky výše')
                film_id = vstup_cislo(1, get_film_row_count())
                print('Zadej id kinosálu z tabulky výše')
                kinosal_id = vstup_cislo(1, get_kinosal_row_count())
                datum_cas = None
                ok = False
                while not ok:
                    try:
                        print('Zadej den promítání')
                        den = vstup_cislo(1, 31)
                        print('Zadej měsíc promítání')
                        mesic = vstup_cislo(1, 12)
                        print('Zadej rok promítání')
                        rok = vstup_cislo(1900, date.today().year)
                        print('Zadej hodinu promítání')
                        hodina = vstup_cislo(10, 23)
                        print('Zadej minutu promítání')
                        minuta = vstup_cislo(0, 59)
                        datum_cas = datetime(rok, mesic, den, hodina, minuta)
                        print(datum_cas)
                        ok = True
                    except:
                        print('Chyba v datumu, zkuste to znovu')
                print('Potvrďte úpravu promítání (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    change_promitani(id, film_id, kinosal_id, datum_cas)
                    print('Promítání bylo úspěšně upraveno')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Úprava promítání byla zrušena')
        elif volba == 15:
            if not get_reziser_row_count() == 0:
                print('Režiséři')
                print(get_all_reziser())
                print('Zadej id režiséra z tabulky výše')
                id = vstup_cislo(1, get_reziser_row_count())
                print('Zadej jméno režiséra')
                jmeno = vstup_text()
                print('Zadej příjmení režiséra')
                prijmeni = vstup_text()
                print('Potvrďte úpravu režiséra (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    change_reziser(id, jmeno, prijmeni)
                    print('Režisér byl úspěšně upraven')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Úprava režiséra byla zrušena')
        elif volba == 16:
            if not get_film_row_count() == 0:
                print('Filmy')
                print(get_all_prehled_filmu())
                print('Promítání')
                print(get_all_promitani())
                print('Zadej id filmu z tabulky výše')
                id = vstup_cislo(1, get_film_row_count())
                print('Potvrďte smazání filmu, čímž se smažou i veškerá promítání tohoto filmu (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    remove_promitani_by_film_id(id)
                    remove_film(id)
                    print('Všechna promítání tohoto filmu byla úspěšně smazána')
                    print('Film byl úspěšně smazán')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Smazání filmu bylo zrušeno')
        elif volba == 17:
            if not get_kinosal_row_count() == 0:
                print('Kinosály')
                print(get_all_kinosal())
                print('Promítání')
                print(get_all_promitani())
                print('Zadej id kinosálu z tabulky výše')
                id = vstup_cislo(1, get_kinosal_row_count())
                print('Potvrďte smazání kinosálu, čímž se smažou i veškerá promítání v tomto kinosálu (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    remove_promitani_by_kinosal_id(id)
                    remove_kinosal(id)
                    print('Všechna promítání v tomto kinosálu byla úspěšně smazána')
                    print('Kinosál byl úspěšně smazán')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Smazání kinosálu bylo zrušeno')
        elif volba == 18:
            if not get_promitani_row_count() == 0:
                print('Promítání')
                print(get_all_prehled_promitani())
                print('Zadej id promítání z tabulky výše')
                id = vstup_cislo(1, get_promitani_row_count())
                print('Potvrďte smazání promítání (1...ano, 2...ne)')
                potvrzeni = vstup_cislo(1, 2)
                if potvrzeni == 1:
                    remove_promitani(id)
                    print('Promítání bylo úspěšně smazáno')
                    DatabaseConnectionSingleton.commit_transaction()
                    DatabaseConnectionSingleton.begin_transaction()
                else:
                    print('Smazání promítání bylo zrušeno')
        elif volba == 19:
            print(get_all_celkovy_promitaci_cas())
        else:
            print('konec programu')
            DatabaseConnectionSingleton.commit_transaction()
            DatabaseConnectionSingleton.close_connection()
            sys.exit()
