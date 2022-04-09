# Merkúr;0;0.0562
class Bolygok:
  def __init__(self,sor):
    nev,holdszam,terfogat_arany = sor.strip().split(";")
    self.nev = nev
    self.holdszam = int(holdszam)
    self.terfogat_arany = float(terfogat_arany)

with open("solsys.txt","r",encoding="UTF-8") as f:
  lista = [Bolygok(sor) for sor in f]

print("1. feladat: ")
szam = int(input("     Írj be egy egész számot: "))
szoveg = input("     Írj be egy szöveget: ")

szam = szam ** 2
szoveg = szoveg.lower()
print("     OP: ",end="")
for _ in range(szam):
    print(szoveg, end=" ")

print()

print("2. feladat: ")
a = float(input("     add meg az [a] értékét: "))
b = float(input("     add meg az [b] értékét: "))
c = float(input("     add meg az [c] értékét: "))

if a < b + c or b < a + c or c < a + b:
  print("     létezhet a háromszög ilyen hosszakkal")
else:
  print("     nem létezhet a háromszög ilyen hosszakkal")

t_derek_1 = (a * b) / 2
t_derek_2 = (c * b) / 2
t_derek_3 = (a * c) / 2

egyenlo_szaru_magassag = (b**2 - a**2 / 4 )** 0.5

t_egyenlo_szaru = a * egyenlo_szaru_magassag / 2

if a**2 + b**2 == c**2:
  print("     ez a háromszög derékszögű")
  print(f"     a háromszög kerülete: {a+b+c}")
  print(f"     a háromszög kerülete: {t_derek_1}")

if c**2 + b**2 == a**2:
  print("     ez a háromszög derékszögű")
  print(f"     a háromszög kerülete: {a+b+c}")
  print(f"     a háromszög kerülete: {t_derek_2}")

if a**2 + c**2 == b**2:
  print("     ez a háromszög derékszögű")
  print(f"     a háromszög kerülete: {a+b+c}")
  print(f"     a háromszög kerülete: {t_derek_3}")

if a == b:
  print("     ez a háromszög egyenlő szárú ")
  print(f"     a háromszög kerülete: {a + b * 2}")
  print(f"     a háromszög kerülete: {t_egyenlo_szaru}")  
else:
  print("     ez a háromszög NEM egyenlő szárú ")
  
print("3. feladat:")
print(f"     3.1: {len(lista)} bolygó van a naprendszerben")

holdak = [sor.holdszam for sor in lista]

ossz = sum(holdak)
atlag = ossz / len(holdak)

print(f"     3.2: a naprendszerben egy bolygónak átlagosan {atlag} holdja van")

legnagyobb = max([(sor.terfogat_arany,sor.nev) for sor in lista])[1]

print(f"     3.3:a legnagyobb térfogatú bolygó a {legnagyobb}")

bekeres = input("     3.4: írd be a keresett bolygó nevét: ")
bekeres = bekeres.lower()
bekeres = bekeres.capitalize()
kereso = [sor.nev for sor in lista if bekeres == sor.nev]

if len(kereso) > 0:
  print("          van ilyen nevű bolygó a naprendszer")
else:
  print("             sajnos nincs ilyen nevű bolygó a naprendszer")  

bekeres2 = int(input("     3.5: Írj be egy egész számot: "))

tobb_hold = [sor.nev for sor in lista if bekeres2 < sor.holdszam]

print(f"     a következő bolygókank 10-nál/nél több holdja:\n     {tobb_hold}")