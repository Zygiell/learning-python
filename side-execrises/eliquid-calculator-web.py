from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def rozcieczacz():
    vga, vgb, vgc = 0, 0, 0
    args = request.args
    aromat = args.get("aromat")  #ile aromatu w buteleczce
    vessel = args.get("vessel") #pojemność buteleczki
    desiredPg = args.get("desiredPg")
    nicotineBasePg = args.get("nicotineBasePg")
    nicotineBase = 0

    if vessel:
        aromat = int(aromat)
        vessel = int(vessel)
        pgTotal = int(vessel) * (int(desiredPg)/100)#
        pgToBeAdded = pgTotal - aromat #ile trzeba PG aby osiągnąć "desired %PG"
        nicotineBase = pgToBeAdded / (int(nicotineBasePg)/100) #Ile dodać bazy nikotynowej
        vga = vessel
        vgb = nicotineBase
        vgc = aromat
        

    return """<!DOCTYPE html>
<html>
<body>

<h2>Kalkulator rozcięczania e-liquidu</h2>

<form action="/">
  <label for="aromat">Ile aromatu w ml:</label><br>
  <input type="text" id="aromat" name="aromat" value="6"><br>
  <label for="vessel">Pojemność butelki w ml:</label><br>
  <input type="text" id="vessel" name="vessel" value="60"><br>
  <label for="desiredPg">Ile %PG chcesz osiągnąć:</label><br>
  <input type="text" id="desiredPg" name="desiredPg" value="30"><br>
  <label for="nicotineBasePg">Ile %PG zawiera baza nikotynowa:</label><br>
  <input type="text" id="nicotineBasePg" name="nicotineBasePg" value="40"><br><br>
  <input type="submit" value="Oblicz">
</form> """ + "Ile dolać bazy nikotynowej: " + str(nicotineBase) + " ml" + "<br>" + "Ile dodać VG 100%: " + str(vga - vgb - vgc) + "ml" + """</body>
</html>"""


app.run()
