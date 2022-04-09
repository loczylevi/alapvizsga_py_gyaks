#Britanney Cummings;$55486;1993;Romania
#Kibo Dunlap;$101541;1988;Hungary

class Munkatársak:
  def __init__(self,sor):
    nev,jovedelem,szuletes,helyileg_hol = sor.strip().split(";")
    self.nev = nev
    self.jovedelem = jovedelem.replace('$', '')
    self.szuletes = int(szuletes)
    self.helyileg_hol = helyileg_hol

with open("employees.txt","r",encoding="latin2") as f:
  lista = [Munkatársak(sor) for sor in f]

print("3.feladat:")
print(f"3.2: a cégnél {len(lista)} programozó dolgozik!")

jovedelmek = [int(sor.jovedelem) for sor in lista]
ossz = sum(jovedelmek)
atlag = ossz / len(jovedelmek)

print(f"3.3: az alkalmazottak havi átlag jövedelme: ${atlag:.1f}")
bekeres = input("3.4: írd be a kerestt nevet:")
kereso = [sor for sor in lista if bekeres == sor.nev]

if len(kereso) > 0:
  for sor in kereso:
    print(f"    életkor:    {2022-sor.szuletes}")
    print(f"    székhely:    {sor.helyileg_hol}")
    print(f"    havi fizetés:    {(float(sor.jovedelem) * 361.51):.0f} HUF")
else:
  print("nincs ilyen nevű alkalmazott a cégnél")



