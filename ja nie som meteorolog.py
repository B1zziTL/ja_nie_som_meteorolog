#otvorenie suboru
subor = open("meteo_stanice.txt","r",encoding="utf-8")

#premenne
pocet_merani = 0
teploty = []

#prehladavanie kaydeho riadku v subore
for riadok in subor:
    pocet_merani += 1
    riadocek = riadok.split()
    nieco = float(riadocek[3].replace(',', '.')) #nahradi ciarku bodkou, aby sa zo stringu dal urobit float
    teploty.append(nieco)
    najvyssia = str(max(teploty))
    
    text = najvyssia.replace('.', ',') #nahradi bodku ciarkou, kedze v subore hodnota nie je s bodkou, ale s ciarkou
    #vyhlada najvyssiu hodnotu v texte a priradi k nej stanicu
    if text in riadok:
        stanica = riadocek[0]
    
#vypise pozadovane hodnoty
print('Počet meraní dokopy je: ', pocet_merani)
print('Maximálna teplota: ', najvyssia)
print('Namerané teploty sú:')
print(*teploty, sep=', ')
print('Stanica s najvyššou nameranou teplotou je: ', stanica) 
print('Priemerné teploty sú: ', sum(teploty)/len(teploty))

