import os

print("Na początku podamy liczbę kont, które chcemy utworzyć (zatwierdzamy enterem),")
print("następnie będziemy wypisywać nazwę konta i hasło do konta, oddzielone spacją, tak wypisany zestaw zatwierdzamy enterem,")
print("aż do momentu wypisania wszystkich kont. Konta będę dodawać się do zawsze widocznej listy.")
print("Ani nazwa konta, ani hasło nie mogą zawierać spacji.")
print()

lista = []
iteracja = 0
n = int(input("Ile kont wygenerować? "))
os.system('cls')
with open('konta.bat', 'w', encoding="utf-8") as konta:
    for i in range(n):
        for j in range(iteracja):
            print(lista[j][0], lista[j][1])
        print()
        print("Nazwa_konta Hasło")
        dane = [s for s in input().split()]
        lista.append(dane)
        konta.write("net user "+dane[0]+" "+dane[1] +
                    " /add /passwordchg:no /expires:never\n")
        konta.write("net localgroup Użytkownicy "+dane[0]+" /add\n")
        iteracja = iteracja + 1
        os.system('cls')

for j in range(iteracja):
    print(lista[j][0], lista[j][1])
print()
print('Wygenerowano program wsadowy.')
print('Należy użyć go na komputerze docelowym, uruchamiając jako administrator.')
print()

with open('sciaga.txt', 'w', encoding="utf-8") as sciaga:
    sciaga.write("Nazwa_konta Hasło:\n")
    for j in range(iteracja):
        sciaga.write(lista[j][0]+" "+lista[j][1]+"\n")

"""
Dostępne opcje:

Lista kont użytkowników w systemie: net user
Lista grup użytkowników w systemie: net localgroup
Tworzenie konta użytkownika: net user nazwa_użytkownika /add
Ustawienie hasła użytkownika: net user nazwa_użytkownika hasło_użytkownika
Wymuszenie zmiany hasła użytkownika po zalogowaniu: net user nazwa_użytkownika /logonpasswordchg:yes
Zablokowanie możliwości zmiany hasła użytkownika: net user nazwa_użytkownika /passwordchg:no
Ograniczenie czasu pracy użytkownika: net user nazwa_użytkownika /times:{czas}
Wyświetlenie ustawień konta użytkownika: net user nazwa_użytkownika
Ustawienie daty wygaśnięcia konta użytkownika: net user nazwa_użytkownika /expires:{data}
Ustawienie komentarza dla konta użytkownika: net user nazwa_użytkownika /comment:”treść_komentarza”
Dodatnie pełnej nazwy konta użytkownika: net user nazwa_użytkownika /fullname:”Pełna nazwa”
Dezaktywacja konta użytkownika: net user nazwa_konta /active:no
Dodanie konta użytkownika do grupy lokalnej: net localgroup nazwa_grupy nazwa_konta /add
Usunięcie konta użytkownika: net user nazwa_konta /del

Źródło: https://technikinformatyk.pl/soisk/zarzadzanie-uzytkownikami-za-pomoca-net-user/
"""


# Aktywacja konta administratora jesli potrzebna
# net user administrator /active:yes
