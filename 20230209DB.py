#sprawdzić połączenie
import psycopg2
polaczenie=psycopg2.connect(host="jsystems.pl",database="demo",user="demo",password="demo",port=5432)
kursor = polaczenie.cursor()
sql="select * from owoce"
kursor.execute(sql)
for w in kursor:
    print(w[1])
kursor.close()

#Ważna informacja dla osób równie zeschizowanych na punkcie wydajności co i ja (czyli mam nadzieję również Ciebie szanowny czytelniku ;) ):
# Dane odczytywane są z bazy w momencie wywołania funkcji "execute". Fetch nie n
# astępuje w pętli kursorowej (do czego mogli przywyknąć użytkownicy takich języków jak np. PL/SQL), a od razu w momencie
# wywołania wykonania zapytania.


# modyfikacja elementu i odbieranie id
kursor = polaczenie.cursor()
sql="insert into owoce(nazwa) values ('Arbuz') returning numer"
kursor.execute(sql)
id=str(kursor.fetchone()[0])
print('id='+id)
polaczenie.commit()
kursor.close()

