#Лабароторная работа 3пш
limit = float(input())
records= int(input())
errors=0
exceeded=0
valid=0
total=0.0
peak=0.0
for _ in range(records):
    reading= input()
    if reading == 'error':
        errors+=1
    else:
        reading=float(reading)
        valid+=1
        total+=reading
        if valid ==1 or reading > peak:
            peak= reading
        if reading > limit:
            exceeded+=1
mean= total/valid
print(records)
print(errors)
print(exceeded)
print(f'{peak:.1f}')
print(f'{mean:.1f}')