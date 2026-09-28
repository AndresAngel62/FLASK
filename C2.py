week = ["Lunes","Martes","Miiercoles","Jueves","Viernes","Sabado","Domingo"]
out=[]
for i,day in enumerate (week):
    if day == 'Sabado' or day =='Domingo'or day =='Viernes':
        out.append(i)
print(out)