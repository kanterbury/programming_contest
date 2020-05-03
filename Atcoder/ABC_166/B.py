N, K = list(map(int,input().split()))
d_list = []
A_list = []

result = list(range(1,N+1))

for i in range(K):
  d = int(input())
  A_list = list(map(int,input().split()))
  for j in range(len(A_list)):
    if(A_list[j] in result):
      result.remove(A_list[j])

print(len(result))


