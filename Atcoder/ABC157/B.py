A = [[]*3]*3

for i in range(3):
  A[i] = list(map(int,input().split()))

N = int(input())

B = [int(input()) for i in range(N)]

result = "No"

if(A[0][0] in B and A[0][1] in B and A[0][2] in B):
  result = "Yes"
if(A[1][0] in B and A[1][1] in B and A[1][2] in B):
  result = "Yes"
if(A[2][0] in B and A[2][1] in B and A[2][2] in B):
  result = "Yes"
if(A[0][0] in B and A[1][0] in B and A[2][0] in B):
  result = "Yes"
if(A[0][1] in B and A[1][1] in B and A[2][1] in B):
  result = "Yes"
if(A[0][2] in B and A[1][2] in B and A[2][2] in B):
  result = "Yes"
if(A[0][0] in B and A[1][1] in B and A[2][2] in B):
  result = "Yes"
if(A[0][2] in B and A[1][1] in B and A[2][0] in B):
  result = "Yes"

print(result)