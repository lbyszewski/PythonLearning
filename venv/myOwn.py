

x = int(input("podaj liczbę x: "))
y = int(input("podaj liczbę y: "))

def getFunction(x , y):
    return x + y

def finalResult(x,y):
    return  x * y



def  getResult(x, y):
    if(x >= 3 and y>= 5) :

        return getFunction(x,y)

    else:

        return finalResult(x,y)


final = getResult(x,y)
print(final)


