def main():
    print "Hello world!"

def funkcja():
    print "babala"

def dodawanie(liczba_a, liczba_b):
    rezultat = liczba_a + liczba_b
    return rezultat

def mnozenie(liczba_a, liczba_b):
    rezultat = liczba_a * liczba_b
    return rezultat

def czy_jest_wieksza(liczba_a, liczba_b):
    if liczba_a > liczba_b:
        print "wszedlem_tutaj"
    else:
        print "jestem w elsie"

def mnozenie1(liczba_a, liczba_b):
    rezultat = liczba_a*liczba_b
    if rezultat > 10:
        print "wiekszy"
    else:
        print "mniejszy"

def wydrukuj():
    licznik = 0

    while licznik < 10:
        licznik = licznik + 1
        print "obecna wartosc licznika: " + str(licznik)

def przyklad_z_for():
    for i in range(0, 10):
        print i

przyklad_z_for()
