from generators import gene

x=gene()

print(x)

for a in x:
    print(a)
    print(f'processing {a} going to retreive next')

y = ['ray','ravi','Ajay','ashok','lewis','harry']
result=[i.upper() for i in y]
result2=(i.upper() for i in y)
print(result)
print(result2)

for a in result2:
    print(a)