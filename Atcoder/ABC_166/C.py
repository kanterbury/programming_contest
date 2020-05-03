N, M = list(map(int,input().split()))
H_list = list(map(int,input().split()))
xy = [map(int, input().split()) for _ in range(M)]
x, y = [list(i) for i in zip(*xy)]

result = [True] * N
for i in range(M):
  if(H_list[x[i]-1] > H_list[y[i]-1]):
    result[y[i]-1] = False
  elif(H_list[x[i]-1] < H_list[y[i]-1]):
    result[x[i]-1] = False
  else:
    result[x[i]-1] = False
    result[y[i]-1] = False
print(result.count(True))