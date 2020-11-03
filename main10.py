from generators import gene

x=gene()

print(x)

for a in x:
    print(a)
    print(f'processing {a} going to retreive next')