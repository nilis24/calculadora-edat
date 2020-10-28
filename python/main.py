import datetime

print("BENVINGUT A LA CALCULADORA D'EDAT!")

DiaNaixement = int(input("Introdueix el teu dia de naixement (en numeros): "))
MesNaixement = int(input("Introdueix el teu mes de naixement (en numeros): "))
AnyNaixement = int(input("Introdueix el teu any de naixement (en numeros): "))

DataNaixement = datetime.date(AnyNaixement, MesNaixement, DiaNaixement)

DataAvui = datetime.datetime.now()

DiesEdat = DataAvui.day - DataNaixement.day
MesosEdat = DataAvui.month - DataNaixement.month
AnysEdat = DataAvui.year - DataNaixement.year

print("Vas nèixer al "+DataNaixement.strftime("%d")+"-"+DataNaixement.strftime("%m")+"-"+DataNaixement.strftime("%Y"))
print("Tens "+f"{AnysEdat}"+" anys, "+f"{MesosEdat}"+" mesos i "+f"{DiesEdat}"+" dies.")