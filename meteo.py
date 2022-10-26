subor = open("meteo_stanice.txt","r",encoding="utf-8")

pocet_merani = 0
teploty = []
for riadok in subor:
    pocet_merani += 1
    riadocek = riadok.split()
    teploty.append(riadocek[3])

print("Teploty sú:", ", ".join(teploty))
dokopy = 0
for i in teploty:
    dokopy += i
    print(dokopy)



print("Počet meraní dokopy je: ")

print("Maximálna teplota: ", max(teploty))

