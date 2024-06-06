n = int(input("Quantos números da sequência fibboci: "))
f = 0
fib = [0, 1]

while len(fib) < n:
    sequencia =  fib[-1] + fib[-2]
    fib.append(sequencia)

print(fib)