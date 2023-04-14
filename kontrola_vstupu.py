
def vstup_cislo(min: int, max: int):
    """
    Metoda slouží pro kontrolu vstupu při zadávání čísla z klávesnice do programu.
    Kontroluje vstup do té doby, než je vstup správný

    :param min: minimální hodnota čísla
    :param max: maximální hodnota čísla
    :return: zkontrolovaný číselný vstup
    """
    cislo = None
    ok = False
    while not ok:
        try:
            cislo = int(input())
            ok = min <= cislo <= max
            if not ok:
                print("Zadané číslo není v rozsahu od {} do {}".format(min, max))
        except:
            print("Chyba ve vstupu, zkuste to znovu")
    return cislo


def vstup_text(min: int = 2, max: int = 50):
    """
    Metoda slouží pro kontrolu vstupu při zadávání textu z klávesnice do programu.
    Kontroluje vstup do té doby, než je vstup správný

    :param min: minimální počet znaků vstupního textu, defaultní hodnota = 1 -> minimálně jeden znak
    :return: zkontrolovaný textový vstup
    """
    text = None
    ok = False
    while not ok:
        try:
            text = input()
            if max >= len(text) >= min:
                ok = True
            else:
                print("Délka zadaného řetězce neodpovídá požadované délce {} - {} znaků".format(min, max))
        except:
            print("Chyba ve vstupu, zkuste to znovu")
    return text
