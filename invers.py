numeros=[10,2,5,6,8]
nuevalista=[]
cambio=True
index = len(numeros) - 1
while (index >= 0):
  nuevalista.append(numeros[index])
  index = index - 1

print(nuevalista)

for index in range(len(numeros)//2):
    numeros[index],numeros[len(numeros)-index-1]=numeros[len(numeros)-index-1],numeros[index]
print(numeros)