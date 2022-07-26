n = int(input("Insira a quantidade de números: "))
inteiros = []
for i in range(0,n,1):
    inteiros.append(input().split(' '))
for num in range(0,len(inteiros),2):
    a = list(map(int, inteiros))
    print(a, end = ' ')