import time
"""
def Fib_R(position):
    if(position==1):
        return 0
    else:
        if(position==2):
            return 1
        else:
            return Fib_R(position-1) + Fib_R(position-2)

for i in range(1, 101):
    inicio = time.time()
    aux=Fib_R(i)
    fim = time.time()
    tempo = fim-inicio
    print(i,';',aux,';',tempo)
    result=(i,aux,tempo)
    writer = open('Fib_R.txt','a')
    writer.write(str(result))
    writer.write('\n')
writer.close()


"""


def Fib_I (position):
    n=position
    if (position == 1):
        return 0

    else:
        if (position == 2):
            return 1
        else:
            first = 0
            second = 1

            for i in range(2, n):


                value = first + second
                first = second
                second = value
                #print(i, value, tempo)



        return value


for position in range(1, 101):
    inicio=time.time()
    aux=Fib_I(position)
    fim = time.time()
    tempo = fim-inicio
    print(aux)
    result=(position,aux,tempo)
    writer = open('Fib_I.txt','a')
    writer.write(str(result))
    writer.write('\n')
writer.close()