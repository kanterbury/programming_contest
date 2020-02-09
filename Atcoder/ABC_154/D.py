N, K = list(map(int,input().split()))
p_list = list(map(int,input().split()))

sum = 0
for k in range(K):
  sum += p_list[k]
max = sum

i = 0
while(i + K  < N):
  sum = sum - p_list[i] + p_list[i+K]
  if(sum > max):
    max = sum
  i += 1

print(0.5 * (max+K))