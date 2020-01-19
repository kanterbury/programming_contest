N = int(input())
P_list = list(map(int,input().split()))

min_num = 2 * 10**5 + 1

count = 0

for i in range(N):
  if(P_list[i] <= min_num):
    count += 1
    min_num = P_list[i]

print(count)
