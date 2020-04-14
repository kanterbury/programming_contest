S = input()
Q = int(input())
T = [input() for i in range(Q)]

left = ""
right = ""

for i in range(Q):
  s = T[i]
  if(int(s[0]) == 2):
    if(int(s[2]) == 1):
      left = s[4] + left
    else:
      right = right + s[4]
  else:
    S = left + S + right
    S = S[::-1]
    left = ""
    right = ""
S = left + S + right

print(S)