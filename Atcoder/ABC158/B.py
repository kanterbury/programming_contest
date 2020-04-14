N, A, B = list(map(int,input().split()))

waru = int(N / (A + B))
amari = N % (A + B)

result = waru * A

if(amari > A):
  result += A
else:
  result += amari

print(result)