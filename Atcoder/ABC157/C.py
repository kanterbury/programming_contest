N, M = list(map(int,input().split()))

s = []
c = []
for i in range(M):
    x1,y1=[int(i) for i in input().split()]
    s.append(x1)
    c.append(y1)

sum = 0
flag = True

if(N == 1 and M == 0):
  print(0)
  exit()

for i in range(M):
  if(s[i] == 1 and c[i] == 0 and N != 1):
    print(-1)
    exit()
  for j in range(M):
    if(s[i] == s[j] and c[i] != c[j]):
      print(-1)
      exit()

kisyutu = []

for i in range(M):
    if not(s[i] in kisyutu):
      sum += c[i] * (10 ** (N - s[i]))
      kisyutu.append(s[i])
if not(1 in s):
  sum += 10 ** (N - 1)
print(sum)

