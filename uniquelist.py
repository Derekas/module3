numeros=[10,2,3,4,4,4,3,3,3,56,7]
unique=[]
for i in numeros:
    if i not in unique:
        unique.append(i)
print(unique)
