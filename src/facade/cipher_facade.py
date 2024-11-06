from rot13_cipher import szyfrowanie_rot13, deszyfrowanie_rot13
from src.ciphers.rot47_cypher import szyfrowanie_rot47, deszyfrowanie_rot47
from src.history.history_memory import *
from src.menu.console_menu import *



algorytm_rot_13 = "ROT13"
algorytm_rot_47 = "ROT47"
historia = History_Of_Coding_Decoding()

while True:

    menu = Menu()
    print(menu)
    wybor = menu.wybierz()

    if wybor == "1":
        print(menu.repr_szyfry())
        wybor = menu.wybierz()

        if wybor == "1":
            zdanie_zakodowane = menu.podaj_zdanie_do_zakodowania_dekodowania()
            print(f"\n-------------------\n|kod : {szyfrowanie_rot13(zdanie_zakodowane)}|\n-------------------\n")
            format_do_konwersji_json = (szyfrowanie_rot13(zdanie_zakodowane), algorytm_rot_13, historia.dodaj_czas())
            historia.dodaj(json_maker(format_do_konwersji_json))

        elif wybor == "2":
            zdanie_zakodowane = menu.podaj_zdanie_do_zakodowania_dekodowania()
            print(f"\n-------------------\n|kod : {szyfrowanie_rot47(zdanie_zakodowane)}|\n-------------------\n")
            format_do_konwersji_json = (szyfrowanie_rot47(zdanie_zakodowane), algorytm_rot_47, historia.dodaj_czas())
            historia.dodaj(json_maker(format_do_konwersji_json))

    elif wybor == "2":
        print(menu.repr_szyfry())
        wybor = menu.wybierz()

        if wybor == "1":
            zdanie_zakodowane = menu.podaj_zdanie_do_zakodowania_dekodowania()
            print(f"\n-------------------\n|kod : {deszyfrowanie_rot13(zdanie_zakodowane)}|\n-------------------\n")
            format_do_konwersji_json = (deszyfrowanie_rot13(zdanie_zakodowane), algorytm_rot_13, historia.dodaj_czas())
            historia.dodaj(json_maker(format_do_konwersji_json))

        elif wybor == "2":
            zdanie_zakodowane = menu.podaj_zdanie_do_zakodowania_dekodowania()
            print(f"\n-------------------\n|kod : {deszyfrowanie_rot47(zdanie_zakodowane)}|\n-------------------\n")
            format_do_konwersji_json = (deszyfrowanie_rot47(zdanie_zakodowane), algorytm_rot_47, historia.dodaj_czas())
            historia.dodaj(json_maker(format_do_konwersji_json))

    elif wybor == "4":
        break

    elif wybor == "3":
        historia.pokaz_historie()

    elif wybor == "5":
        sciezka = menu.podaj_sciezke_do_pliku()
        plik = json_loader(sciezka)
        slownik_pliku = json_handler(plik)
        zdanie_zakodowane = slownik_pliku[0]
        algorytm = slownik_pliku[1]
        timestamp = slownik_pliku[2]

        if algorytm == algorytm_rot_13:
            print(f"\n-------------------\n|kod : {deszyfrowanie_rot13(zdanie_zakodowane)}|\n-------------------\n")
            format_do_konwersji_json = (deszyfrowanie_rot13(zdanie_zakodowane), algorytm_rot_13, timestamp)
            historia.dodaj(json_maker(format_do_konwersji_json))
        elif algorytm == algorytm_rot_47:
            print(f"\n-------------------\n|kod : {deszyfrowanie_rot47(zdanie_zakodowane)}|\n-------------------\n")
            format_do_konwersji_json = (deszyfrowanie_rot47(zdanie_zakodowane), algorytm_rot_47, timestamp)
            historia.dodaj(json_maker(format_do_konwersji_json))
        else:
            print("sprawdz czy wpisałes wszystko poprawnie")
    elif wybor == "6":
        sciezka = menu.podaj_sciezke_do_pliku()
        historia.zapisz_historie(sciezka)


    else:
        print("zly wwybor!!!")