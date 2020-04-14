K, N = list(map(int,input().split()))
A = list(map(int,input().split()))

max = K - A[N-1] + A[0]

for i in range(N-1):
  if(max < A[i+1] - A[i]):
    max = A[i+1] - A[i]

  
print(K - max)