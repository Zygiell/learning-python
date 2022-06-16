imie = input("Jak masz na imie?:\n")
print("Cześć", imie)
wiek = int(input("Ile masz lat?:\n"))
print("za rok będziesz mieć", wiek + 1, "lat.")

if(wiek < 30):
    print("Jeszcze nie masz 30 lat")
if(wiek >= 30):
    if(imie == "Kuba"):
        print("Jesteś starym chujem")
    elif(imie[-1] == "a"):
        print("Jesteś starą cipą")
    if(imie[-1] != "a"):
        print ("Jesteś starym chujem")
