N = int(input())
X_list = list(map(int,input().split()))

P = 0
min_sum = 100 ** 2 * 100
while(True):
  sum = 0
  for x in range(N):
    sum += (X_list[x]- P) ** 2
  if(sum <= min_sum):
    min_sum = sum
    P += 1
    continue
  else:
    break

print(min_sum)