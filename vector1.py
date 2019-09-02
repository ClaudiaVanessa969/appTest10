#Ejercicio 1:
#fruits = ["Apple", "Banana", "Orange"]
#print("The first value is: ", fruits[0])
#print("The last value is: " , fruits[2])

#Ejercicio 2:
N = []
i = 1

'''Create list'''
while i <= 10:
    print("Press number", i ,":")
    x = int(input())
    N.append(x)
    i = i+1

'''Show list'''
i = 1
while i < 10:
    print("The value in the pos", i ,"is: ", N[i])
    i = i+1

N.__len__()



