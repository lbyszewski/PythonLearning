

x = int(input("podaj liczbę x: "))
y = int(input("podaj liczbę y: "))

def getFunction(x , y):
    return x + y

def finalResult(x,y):
    return  x * y



def  getResult(x, y):
    if x >= 3 and y>= 5 :
        wynik = getFunction(x,y)
        return print(wynik)

    elif x >= 6 and y >= 8 :
        wynik2 = finalResult(x,y)
        return print(wynik2)


final = getResult(x,y)
print(final)


