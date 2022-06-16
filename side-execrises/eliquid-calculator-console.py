aromat = int(input('Ile aromatu jest w butelce:\n'))  #ile aromatu w buteleczce
vessel = int(input('Jaka jest pojemność butelki:\n')) #pojemność buteleczki
desiredPg = int(input('Ile % PG chcesz osiągnąć:\n'))
pgTotal = vessel * (desiredPg/100)#
nicotineBasePg = int(input('Ile % PG zawiera baza nikotynowa:\n'))
pgToBeAdded = pgTotal - aromat #ile trzeba PG aby osiągnąć "desired %PG"
nicotineBase = pgToBeAdded / (nicotineBasePg/100) #Ile dodać bazy nikotynowej
print(nicotineBase, "ml nicotine base")
print(vessel - nicotineBase - aromat, "ml VG")
