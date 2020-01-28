year=1 
tui=10000
newfee=0 
while year<=10:
    tui = tui*1.5
    year = year + 1
print("Fees in ten year will be:",format(tui,".2f"))
while year<=14:
    tui=tui*1.5
    year = year + 1 
    newfee = newfee + tui
print("The tuition fee in next few years is:",format(newfee,".2f"))