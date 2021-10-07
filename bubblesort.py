numeros=[10,2,5,6,8]
cambio=True
while cambio==True:

    for i in range(len(numeros)-1):
        if numeros[i]>numeros[i+1]:
            numeros[i],numeros[i+1]=numeros[i+1],numeros[i]
            cambio=True
        else:
            break
        print(numeros[i])



    