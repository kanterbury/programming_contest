N, K = list(map(int,input().split()))
A_list = list(map(int,input().split()))

if(len(A_list) == len(set(A_list))):
  print("YES")
else:
  print("NO")