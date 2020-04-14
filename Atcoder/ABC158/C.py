A, B = list(map(int,input().split()))

for i in range(1,10001):
  a = int(i * 0.08)
  if(a == A):
    b = int(i * 0.1)
    if(b == B):
      print(i)
      exit()
print('-1') 
