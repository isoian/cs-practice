#лабораторная работа 4
def winner(names,scores):
    top=0
    for i in range(1,len(scores)):
        if scores[i]>scores[top]:
            top=i
    return names[top]

def average(scores):
    if len(scores)==0:
        return 0.0
    summ=0
    for n in scores:
        summ+=n
    return round(summ/len(scores),2)

def ranking(names,scores):
    indices=sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )
    return [names[i] for i in indices]

def above_average(names,scores):
    nm=[]
    avr= average(scores)
    for i in range(len(scores)):
        if scores[i]>avr:
            nm.append(names[i])
    return nm